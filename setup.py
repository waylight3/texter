from setuptools import setup, find_packages

setup_requires = [
	]

install_requires = [
	]

dependency_links = [
	]

setup(
	name='texter',
	version='0.0.1',
	description='texter the text',
	author='DoHyeon Lee',
	author_email='waylight3@naver.com',
	packages=["ML"],
	include_package_data=True,
	install_requires=install_requires,
	setup_requires=setup_requires,
	dependency_links=dependency_links,
	entry_points={
		'console_scripts': [
			],
		"egg_info.writers": [
				"foo_bar.txt = setuptools.command.egg_info:write_arg",
			],
		},
	)