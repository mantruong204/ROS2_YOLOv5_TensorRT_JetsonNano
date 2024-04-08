from setuptools import setup

package_name = 'ros2_yolov5_pkg'
#yolov5_Det_module="/ros2_yolov5_pkg/yoloDet.py"
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='minhman',
    maintainer_email='minhman@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'real_camera_node = ros2_yolov5_pkg.real_camera_node:main',
            'yolov5_node = ros2_yolov5_pkg.yolov5_node:main'
        ],
    },
)
