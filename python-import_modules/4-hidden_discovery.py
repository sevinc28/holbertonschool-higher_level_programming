#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    names = dir(hidden_4)
    for name in sorted(name for name in names if not name.startswith("__")):
        print(name)
