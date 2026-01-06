## Concurrency & Limitations

- Model loading happens at application startup and is blocking.
  Cold starts can take several minutes depending on network and hardware.

- Inference is CPU-bound and synchronous.
  Each request occupies a worker until completion.

- This service is not designed for high-throughput or concurrent inference.
  Intended for low-volume usage and repeated requests via caching.

- Redis caching reduces repeated computation but does not reduce single-request latency.
