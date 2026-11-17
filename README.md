<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Aymane Aboulhouda — AI & Big Data Engineer" />

</div>

### `> whoami`

```text
name       : Aymane Aboulhouda
role       : AI & Big Data engineering student
school     : UIR (Rabat) x Université de Sherbrooke
degree     : M.Sc. Computer Science, AI & Data Science (double diploma)
location   : Sherbrooke, QC
focus      : distributed pipelines / streaming detection / computer vision / applied GenAI
ethos      : reproducible, measured, self-hosted, local-first
```

### `> ls ~/stack`

```text
languages  : python  c++  typescript  javascript  bash
data       : spark  hive  hdfs  kafka
ml / cv    : opencv  numpy  gradient-boosted-trees  pybind11
web        : react  node.js  astro  tailwind
infra      : docker  linux  git  pi-hole  portainer
```

### `> ls ~/projects`

#### `ocp-intervention-app` &nbsp;`private` &nbsp;`internship · OCP Group`
Industrial maintenance platform with an ML urgency classifier, built as a 4-service containerized system during my engineering internship at OCP (Khouribga).
```text
 react/vite spa :3000 ──REST──▶ express api :5000 ──SQL──▶ postgresql 15
                                      │
                                      └──HTTP /predict──▶ fastapi ml service :8000
                                                          tf-idf + linearsvc (joblib)

 data      11-table relational schema · triggers enforce stock integrity and log every
           part transaction · auto updated_at · indexes on hot query paths · soft deletes
 ml        live urgency prediction while the technician types (debounced preview endpoint);
           predicted_urgency stored apart from the final label, so model drift can be
           measured against human decisions in production
 api       layered express routing · status state machine with automatic timestamps ·
           geocoding of sites via nominatim
 ops       docker compose orchestration · persistent volumes · service dependency ordering
```

#### `lyricflow` &nbsp;`private`
Full-stack generative-AI product: prompt → structured lyrics → full song → cover art, with accounts, a public community feed and a paid tier.
```text
 react + typescript spa ──▶ express api (17 REST endpoints) ──▶ mongodb (mongoose)
        │                        │
        │                        ├──▶ llm   : structured JSON output enforced by response schema
        │                        └──▶ image : server-side proxy, API keys never reach the client
        └──▶ audio : async generation jobs, polled with bounded retries and graceful fallback

 security  jwt sessions · bcrypt password hashing · nosql-injection sanitization
 data      user / song document models · public profiles, comments, ratings, sharing
 client    typed service layer (db, llm, audio, image, upload) · offline cache fallback
```

#### `network-intrusion-detection` &nbsp;`private`
Real-time intrusion detection on live network traffic using a distributed streaming pipeline.
```text
 traffic events ──▶ kafka topics ──▶ spark streaming job ──▶ detections / alerts
```

#### [`distributed-energy-forecasting`](https://github.com/AymaneJoestar/distributed-energy-forecasting)
Distributed big data pipeline for smart-grid consumption forecasting.
```text
 raw meter data ──▶ hdfs (storage) ──▶ hive (warehouse / sql modeling) ──▶ spark mllib
                                                                   gradient-boosted trees
```

#### [`License-Plate-Deblurring-ComputerVision-`](https://github.com/AymaneJoestar/License-Plate-Deblurring-ComputerVision-)
Classical image-restoration pipeline that recovers motion-blurred plates and proves it with metrics.
```text
 blurred plate ──▶ blur estimation ──▶ deconvolution ──▶ evaluation
                   psf angle + length    wiener filter     psnr · ssim
                   (cepstrum / radon)    richardson–lucy   tesseract ocr accuracy

 benchmark  synthetic ground-truth plates with known blur → automated comparison table
 tooling    object-oriented pipeline class · interactive parameter widgets
```

#### [`aymane_tp`](https://github.com/AymaneJoestar/aymane_tp)
Native C++ extension for Python: streaming cumulative median in O(n log n).
```text
 c++ core  ordered set + iterator pinned to the median, rebalanced on each insert
 binding   pybind11 → numpy-compatible python module, pip-installable (setuptools / pyproject)
 quality   pytest suite · sphinx documentation published on read the docs
```

### `> stats`

<div align="center">
<img src="./assets/stats.svg" alt="GitHub stats" />
&nbsp;
<img src="./assets/langs.svg" alt="Top languages" />
</div>

### `> contact`

```text
github     : https://github.com/AymaneJoestar
linkedin   : https://www.linkedin.com/in/aymane-aboulhouda
email      : aymane.aboulhouda@usherbrooke.ca
```
