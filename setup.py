from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pyclearpass',
    url='https://github.com/aruba/pyclearpass',
    author='Aruba Automation',
    author_email='aruba-automation@hpe.com',
    packages=['pyclearpass'],
    install_requires=['requests >=2.24','urllib3 >=1.25.10'],
    version='1.0.7',
    license='MIT',
    description='HPE Aruba Networking ClearPass SDK has been developed in Python v3.9 to utilise the full functionality of the HPE Aruba Networking ClearPass REST API environment. Each available REST API command is available for use in this package.',
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
    project_urls={"repository":"https://github.com/aruba/pyclearpass/","changelog":"https://github.com/aruba/pyclearpass/blob/main/RELEASE-NOTES.md","homepage":"https://developer.arubanetworks.com/aruba-cppm/docs/getting-started-with-pyclearpass"},
    keywords="Aruba, Aruba ClearPass, Aruba CPPM, CPPM, pyclearpass, HPE Aruba Networking ClearPass"
)