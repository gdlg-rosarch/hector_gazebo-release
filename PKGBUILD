# Script generated with Bloom
pkgdesc="ROS - hector_gazebo_plugins provides gazebo plugins from Team Hector. Currently it contains a 6wd differential drive plugin, an IMU sensor plugin, an earth magnetic field sensor plugin, a GPS sensor plugin and a sonar ranger plugin."
url='http://ros.org/wiki/hector_gazebo_plugins'

pkgname='ros-kinetic-hector-gazebo-plugins'
pkgver='0.5.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gazebo'
'ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
)

depends=('gazebo'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-gazebo-ros'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=hector_gazebo_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_gazebo_plugins $srcdir/hector_gazebo_plugins
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

