#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pathlib
from dotenv import load_dotenv

base_path = (pathlib.Path(__file__)).parent.parent
sys.path.append(str(base_path))
from convert2vars import main

if __name__ == '__main__':
    load_dotenv(os.environ.get("DOTENV_FILE"))
    main()
