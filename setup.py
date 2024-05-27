import setuptools

with open("README.md","r",encoding= "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "HDPE_and_PET_Bottle_Plastic_Waste_Classification_Project"
AUTHOR_USERNAME = "PiyushChaudhari99"
SRC_REPO = "cnnImageClassifier"
AUTHOR_EMAIL = "piyushpchaudhari@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USERNAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "bug Tracker" :f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where = 'src')
)