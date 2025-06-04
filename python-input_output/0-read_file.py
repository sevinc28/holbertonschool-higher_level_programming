#!/usr/bin/python3
"""
#bu modul (UTS-8 formatinda) oxuyan ve mezmunu cap eden funksiyani ehate edir
"""
def read_file(filename=""):
    """
    Funksiya UTS-8 formatinda oxuyur
    """
    Args:
        filename(str):faylin adidir
    """
     with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

