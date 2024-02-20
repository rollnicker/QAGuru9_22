def abs_path_from_project(relative_path: str):
    import QAGuru9_22
    from pathlib import Path

    return (
        Path(QAGuru9_22.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
