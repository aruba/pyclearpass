from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pyclearpass',
    url='https://github.com/aruba/pyclearpass',
    author='Aruba Automation',
    author_email='aruba-automation@hpe.com',
    packages=['pyclearpass'],
    install_requires=['requests >=2.24','urllib3 >=1.25.10'],
    version='1.0.1',
    license='MIT',
    description='Aruba ClearPass SDK has been developed in Python v3.9 to utilise the full functionality of the Aruba ClearPass REST API environment. Each available REST API command is available for use in this module.',
    long_description=open('README.md').read(),
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
	"Intended Audience :: System Administrators",
	"Intended Audience :: Automation Experts",
	"Intended Audience :: Deployment Engineers",
    "Topic :: System :: Networking",
    "Natural Language :: English",],
    project_urls={"Source": "https://github.com/aruba/pyclearpass/"},
    keywords="Aruba, Aruba ClearPass, Aruba CPPM, CPPM, pyclearpass"

)