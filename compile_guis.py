# Stolen from a group project between myself and a few others.  All of the work on this file was done by
#  https://github.com/mrkirby153, a member of the project
# But I believe he adapted this from things he found online and from the GUI making program anyways :shrug:

import glob
import optparse
import os.path

from PyQt5.uic.driver import Driver as UICDriver
from PyQt5.uic.exceptions import NoSuchClassError, NoSuchWidgetError


def main():
    globs = glob.iglob('./**/*.ui', recursive=True)
    for filename in globs:
        file, extension = os.path.splitext(filename)
        file_name = os.path.basename(file)
        dir_name = os.path.dirname(file)
        new_filename = f'ui_{file_name}.py'
        output_path = os.path.join(dir_name, new_filename)

        print(f'Compiling UI file {filename} -> {output_path}')

        args = {
            'preview': False,
            'output': output_path,
            'execute': False,
            'debug': False,
            'indent': 4,
            'import_from': None,
            'from_imports': False,
            'resource_suffix': '_rc'
        }

        args = optparse.Values(args)

        driver = UICDriver(args, filename)

        exit_status = 1

        try:
            exit_status = driver.invoke()

        except IOError as e:
            driver.on_IOError(e)

        except SyntaxError as e:
            driver.on_SyntaxError(e)

        except NoSuchClassError as e:
            driver.on_NoSuchClassError(e)

        except NoSuchWidgetError as e:
            driver.on_NoSuchWidgetError(e)

        except Exception as e:
            driver.on_Exception(e)

        print(f'Compile completed with exit code: {exit_status}')


if __name__ == "__main__":
    main()
