from distutils.core import setup

setup(
    name="urdf_parser_py",
    packages=['urdf_parser_py', 'urdf_parser_py.xml_reflection'],
    package_dir={'': 'src'}
)