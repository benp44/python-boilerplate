import tempfile

import nox

# Default sessions to run
nox.options.sessions = "lint", "tests"


LINT_PLUGINS = ["flake8-black", "flake8-import-order", "flake8-bugbear", "flake8-bandit"]
LINT_LOCATIONS = ["src", "tests", __file__]


def install_with_constraints(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run("poetry", "export", "--dev", "--format=requirements.txt", f"--output={requirements.name}", external=True)
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python="3.8")
def tests(session):
    install_with_constraints(session, "pytest")
    session.run("pytest", "--cov")


@nox.session(python="3.8")
def lint(session):
    install_with_constraints(session, "flake8", *LINT_PLUGINS)
    session.run("flake8", *LINT_LOCATIONS)


@nox.session(python="3.8")
def black(session):
    install_with_constraints(session, "black")
    session.run("black", *LINT_LOCATIONS)
