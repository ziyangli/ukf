import os
import platform
import ctypes
import subprocess
import distutils.command.build_py
from distutils.core import setup


class build_cukf(distutils.command.build_py.build_py):
    description = """Build the CUKF shared library"""

    def run(self):
        subprocess.call("cmake . && make cukf && cp -r c ./python/ukf/",
                        shell=True,
                        cwd=os.path.dirname(os.path.abspath(__file__)))
        subprocess.call("cmake . && make c66ukf && cp -r ccs-c66x ./python/ukf/",
                        shell=True,
                        cwd=os.path.dirname(os.path.abspath(__file__)))
        self.data_files = self.get_data_files()
        distutils.command.build_py.build_py.run(self)


setup(
    name="ukf",
    url="https://github.com/sfwa/ukf",
    author="Daniel Dyer",
    author_email="",
    version="1.0.0",
    description="UKF library for UAV state estimation",
    long_description=open("README.md").read(),
    package_dir={"": "python"},
    packages=["ukf"],
    package_data={"ukf": ["c/cukf.dll", "c/libcukf.so", "c/libcukf.dylib",
                          "ccs-c66x/c66ukf.dll", "ccs-c66x/libc66ukf.so",
                          "ccs-c66x/libc66ukf.dylib"]},
    license="MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries"
    ],
    cmdclass={"build_py": build_cukf}
)
