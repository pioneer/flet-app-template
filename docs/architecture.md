# Architecture

The entry point is [src/main.py](../src/main.py). Importing it does not launch UI.
It loads central settings, configures logging and exception hooks, and calls the
imperative Flet application. No decorators or declarative component framework.

```text
src/main.py                 composition / startup
src/app/config.py          validated environment configuration
src/app/logging_config.py  logging policy and exception reporting
src/app/application.py     page lifecycle and event boundary
src/app/ui/home.py         minimal presentation
src/app/domain/            pure decisions, no Flet imports
assets/                   canonical maintained assets
tests/                    non-GUI behavior and task contract tests
tasks.py                  the sole project automation interface
```

Dependencies point inward: UI -> application services -> domain. When the first
real use case needs orchestration, add a small module in `app/services`; when it
needs external I/O, introduce an adapter in `app/infrastructure`. A service owns
that adapter's contract and can receive a fake in tests. Do not create empty
packages, generic repositories, dependency injection containers, or abstract
base classes in anticipation of features.

UI owns controls and navigation, not business decisions or raw HTTP/database
calls. Domain functions use Python types and return results or raise meaningful
exceptions. Services decide retry, timeout, cancellation, and user-facing failure
semantics. Adapters expose expected errors without hiding unexpected failures.

Configuration reads are centralized in `Settings.from_env`. Explicit `APP_DEBUG`
overrides the temporary packaged debug marker. Invalid values fail early, without
echoing potentially sensitive input. There is no dotenv loader or automatic
credential discovery in application code.

Do not block Flet's event loop with slow I/O. Use async APIs where supported and
await their results; own and observe background tasks, including cancellation.
Never leave detached failures as an invisible state change. UI handlers translate
known failures into an appropriate state; log unexpected failures with traceback
at the boundary and preserve the failure rather than silently returning success.

`assets/` is the single source. Flet packaging expects assets inside its app path,
so Invoke copies it to ignored `src/assets/` before build/mobile debug. Never edit
the staged copy. Generated Flutter files and native icons live under `build/`.
Run one build/mobile-debug task at a time in a checkout because they share staging.

No remote services, persistence, analytics, authentication, or networking features
are part of the template. Add only dependencies required by an actual use case.