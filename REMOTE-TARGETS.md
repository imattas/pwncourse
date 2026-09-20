# Remote CTF target mode

Every exploit defaults to a local process. To use an authorized CTF instance, set the target explicitly in WSL:

```bash
export PWN_REMOTE=1
export PWN_HOST=instance.example.ctf
export PWN_PORT=31337
python3 solve.py
```

Remote mode defaults to `127.0.0.1`; only the port is required. Start a local remote-style service with:

```bash
bash scripts/serve-lab.sh labs/05-rop/rop-call/challenge 31337
PWN_REMOTE=1 PWN_PORT=31337 python3 labs/05-rop/rop-call/solve.py
```

The course does not discover targets, bypass authentication, or provide credentials. Challenge-specific TLS, login, banner, and flag-submit behavior belongs in that challenge's README and must be authorized by the competition/platform rules.

For a local run, unset the variables:

```bash
unset PWN_REMOTE PWN_HOST PWN_PORT
python3 solve.py
```
