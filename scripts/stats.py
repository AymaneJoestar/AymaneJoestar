"""Generate terminal-style GitHub stats cards (assets/stats.svg, assets/langs.svg).

Uses STATS_TOKEN if set (a PAT with read access to private repos, so their
languages count), otherwise the workflow's GITHUB_TOKEN (public repos only).
"""
import json
import os
import urllib.request
from collections import Counter
from html import escape

USER = os.environ.get("GH_USER", "AymaneJoestar")
TOKEN = os.environ.get("STATS_TOKEN") or os.environ["GITHUB_TOKEN"]
PRIVATE = bool(os.environ.get("STATS_TOKEN"))

QUERY = """
query($login: String!, $privacy: RepositoryPrivacy) {
  user(login: $login) {
    createdAt
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: $privacy) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

BG, BORDER = "#080d0b", "#1a2e26"
DIM, TEXT, ACCENT, HEAD = "#4d6b5e", "#c9d6cf", "#5fd4a0", "#e6f2ec"
FONT = "'JetBrains Mono','Fira Code','Courier New',monospace"
SKIP = {"HTML", "CSS", "Makefile", "Dockerfile", "Shell", "Batchfile", "Jupyter Notebook"}


def gql():
    body = json.dumps({"query": QUERY, "variables": {"login": USER, "privacy": None if PRIVATE else "PUBLIC"}})
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body.encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]["user"]


def frame(w, h, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="6" fill="{BG}" stroke="{BORDER}"/>
<g font-family="{FONT}">
<text x="24" y="34" font-size="13" fill="{DIM}">$ <tspan fill="{HEAD}">{escape(title)}</tspan></text>
{body}
</g>
</svg>
"""


def stats_card(u):
    c = u["contributionsCollection"]
    repos = u["repositories"]
    stars = sum(r["stargazerCount"] for r in repos["nodes"])
    rows = [
        ("contributions (1y)", c["contributionCalendar"]["totalContributions"]),
        ("commits (1y)", c["totalCommitContributions"] + c["restrictedContributionsCount"]),
        ("pull requests (1y)", c["totalPullRequestContributions"]),
        ("repositories", repos["totalCount"]),
        ("stars", stars),
        ("on github since", u["createdAt"][:4]),
    ]
    body = ""
    for i, (k, v) in enumerate(rows):
        y = 66 + i * 24
        body += (
            f'<text x="24" y="{y}" font-size="13" fill="{TEXT}">{escape(k)}</text>'
            f'<text x="356" y="{y}" font-size="13" fill="{ACCENT}" text-anchor="end">{v}</text>\n'
        )
    return frame(380, 66 + 6 * 24 + 4, "gh stats", body)


def langs_card(u):
    totals = Counter()
    colors = {}
    for r in u["repositories"]["nodes"]:
        for e in r["languages"]["edges"]:
            name = e["node"]["name"]
            if name in SKIP:
                continue
            totals[name] += e["size"]
            colors[name] = e["node"]["color"] or ACCENT
    top = totals.most_common(6)
    total = sum(s for _, s in top) or 1
    body = ""
    for i, (name, size) in enumerate(top):
        pct = size / total * 100
        y = 66 + i * 24
        bar = max(2, round(pct / 100 * 150))
        body += (
            f'<text x="24" y="{y}" font-size="13" fill="{TEXT}">{escape(name)}</text>'
            f'<rect x="168" y="{y-10}" width="150" height="8" rx="2" fill="{BORDER}"/>'
            f'<rect x="168" y="{y-10}" width="{bar}" height="8" rx="2" fill="{colors[name]}"/>'
            f'<text x="356" y="{y}" font-size="13" fill="{ACCENT}" text-anchor="end">{pct:.1f}%</text>\n'
        )
    scope = "public + private repos" if PRIVATE else "public repos"
    body += f'<text x="24" y="{66 + 6 * 24 - 10}" font-size="11" fill="{DIM}">{scope} · notebooks excluded · names hidden</text>\n'
    return frame(380, 66 + 6 * 24 + 4, "top languages", body)


if __name__ == "__main__":
    u = gql()
    os.makedirs("assets", exist_ok=True)
    with open("assets/stats.svg", "w") as f:
        f.write(stats_card(u))
    with open("assets/langs.svg", "w") as f:
        f.write(langs_card(u))
    print("ok", "private" if PRIVATE else "public-only")
