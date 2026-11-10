"""Scan → analyze each file → link files together. Pure function of the project folder."""
from __future__ import annotations

from pathlib import Path

from . import analyzers, leaving
from .connect import link
from .inventory import list_files, load
from .model import Project


def analyze_project(root: Path, name: str | None = None, excludes: list[str] | None = None) -> Project:
    root = root.resolve()
    paths, git = list_files(root, excludes)
    files = load(root, paths)
    project = Project(name=name or root.name, root=str(root), files=files, git=git)
    for f in files:
        analyzers.analyze(f, project.facts)
    link(project)
    leaving.collect(project)
    return project
