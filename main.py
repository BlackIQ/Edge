import config.config as config

import termcolor
import sys
import os

output = config.output_dir

try:
    sys.argv[1]
    
    if sys.argv[1] == "--new":
        try:
            sys.argv[2]
            try:
                sys.argv[3]

                if sys.argv[3] == "--fa":
                    os.system(f"mkdir {output}/posts/{sys.argv[2]}")
                    os.system(f"cp -r files/fa.html {output}/posts/{sys.argv[2]}")
                    os.system(f"mv {output}/posts/{sys.argv[2]}/fa.html {output}/posts/{sys.argv[2]}/index.html")

                    print(termcolor.colored("Post created", "green"))
                elif sys.argv[3] == "--en":
                    os.system(f"mkdir {output}/posts/{sys.argv[2]}")
                    os.system(f"cp -r files/en.html {output}/posts/{sys.argv[2]}")
                    os.system(f"mv {output}/posts/{sys.argv[2]}/en.html {output}/posts/{sys.argv[2]}/index.html")

                    print(termcolor.colored("Post created", "green"))
                else:
                    print(termcolor.colored("Language didn't found", "red"))
            except:
                print(termcolor.colored("Enter the language", "red"))
        except:
            print(termcolor.colored("Enter a post name", "red"))
    else:
        print(termcolor.colored("No match cases", "red"))
        print(termcolor.colored("Try --help or --h to get more information", "yellow"))
except:
    print(termcolor.colored("At least enter on argument", "red"))