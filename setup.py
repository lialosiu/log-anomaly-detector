""" Setup.py for packaging log-anomaly-detector as library """
from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PKG = [
    "Click",
    "elasticsearch5",
    "urllib3==1.21.1",
    "gensim",
    "matplotlib",
    "numpy",
    "pandas",
    "prometheus_client",
    "Flask",
    "scikit-learn",
    "scipy",
    "tqdm",
    "Flask-SQLAlchemy",
    "PyMySQL",
    "sompy",
    "pyyaml",
]

setup(
    name="scorpio",
    version="0.0.1-rc2",
    py_modules=['app'],
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=False,
    classifiers=(
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ),
    python_requires=">3.5",
    url="https://github.com/AICoE/log-anomaly-detector",
    author="Zak Hassan",
    author_email="zak.hassan@redhat.com",
    description="Log anomaly detector for streaming logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    dependency_links=[
	"git+https://github.com/sevamoo/SOMPY.git@76b60ebd6ffd550b0f7faaf632451dfd68827bf7#egg=sompy",
    ],
    install_requires=REQUIRED_PKG,
    entry_points="""
        [console_scripts]
        scorpio=app:cli
    """,
)
