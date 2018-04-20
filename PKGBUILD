# Script generated with Bloom
pkgdesc="ROS - hector_gazebo_thermal_camera provides a gazebo plugin that produces simulated thermal camera images. The plugin uses modified code from the gazebo_ros_camera plugin."
url='http://ros.org/wiki/hector_gazebo_thermal_camera'

pkgname='ros-kinetic-hector-gazebo-thermal-camera'
pkgver='0.5.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gazebo'
'ros-kinetic-catkin'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-roscpp'
)

depends=('gazebo'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=hector_gazebo_thermal_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_gazebo_thermal_camera $srcdir/hector_gazebo_thermal_camera
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

