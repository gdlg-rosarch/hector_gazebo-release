Name:           ros-indigo-hector-gazebo-thermal-camera
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS hector_gazebo_thermal_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_gazebo_thermal_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-driver-base
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
BuildRequires:  gazebo-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-driver-base
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-gazebo-plugins
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp

%description
hector_gazebo_thermal_camera provides a gazebo plugin that produces simulated
thermal camera images. The plugin uses modified code from the gazebo_ros_camera
plugin.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 21 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.6-0
- Autogenerated by Bloom

* Mon Feb 23 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

