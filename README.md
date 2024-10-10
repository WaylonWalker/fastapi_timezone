## Timezone Aware FastApi Application

This is a demo application to demo how someone might make a fastapi application
timezone aware. It does this by injecting a small amount of javascript in the
template to set a timezone cookie that will be passed to the backend on every
request. Alternatively the `X-Timezone` header can override this for non-browser
based http requests i.e. another backend service or curl.

## Running the application

This project uses [just](https://github.com/casey/just) as a command runner, and
[uv](https://github.com/astral-sh/uv) as the package installer, you will need to
have these installed to follow the instructions.

```bash
just run
```

Now you can open the application in your webbrowser at localhost:8000. You will
see the time returned is localized to you even though the simulated times stored
in the database are utc.
