from setuptools import setup, find_packages

long_description = """Experimental package to explore financila analysis"""

setup(name='tsa',
      version='0.1',
      description='Anomaly analysis experimental library',
      author='Yevgeniy Yermoshin',
      author_email='yev.developer@gmail.com',
      license='Apache 2.0',
      long_description=long_description,
      keywords=['pandas', 'data', 'analysis', 'ml', 'time', 'series'],
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)