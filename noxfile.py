"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session

nox.options.sessions = (
    "docs",
)

@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")

    if session.interactive:
        session.run("mkdocs", "serve")
    else:
        session.run("mkdocs", "build")

@nox.session(name="docs-deploy")
def docs_deploy(session: Session) -> None:
    """Deploy the documentation on Github Pages."""
    args = session.posargs
    session.install("-r", "docs/requirements.txt")
    session.run("mkdocs", "gh-deploy", *args)
