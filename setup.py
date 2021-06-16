from setuptools import setup, find_packages


setup(name='hello',
      version='1.0',
      description='Python Distribution Utilities Hello',
      author='nekotrek',
      author_email='nekotrek@python.net',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'helloshiv=client.main:main',
          ],
      },
      install_requires=['requests>=2.25.1'],
      python_requires='>= 3.6'
      #   package_data={
      #       'client': ['config/\.env']
      #   },
      # 下面这么写，就会把脚本拷贝到可执行路径里面，你就可以在全局运行 shiv-hello.sh
      #   scripts=['scripts/shiv-hello.sh'],
      )
