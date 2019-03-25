from setuptools import setup, find_packages

setup(name='django-microservices',
      version='0.2.4',
      description='A framework for building microservices with Django.',
      # This is a fork of https://github.com/lander2k2/django-microservices
      url='https://github.com/hlongmore/django-microservices',
      author='Richard Lander, Henry Longmore',
      author_email='henry@longmore.org',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['django'],
      zip_safe=False)
