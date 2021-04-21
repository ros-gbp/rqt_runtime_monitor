%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rqt-runtime-monitor
Version:        0.5.9
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_runtime_monitor package

License:        BSD
URL:            http://wiki.ros.org/rqt_runtime_monitor
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-rospkg
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-python-qt-binding >= 0.2.19
Requires:       ros-noetic-qt-gui
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rqt-gui
Requires:       ros-noetic-rqt-gui-py
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_runtime_monitor provides a GUI plugin viewing DiagnosticsArray messages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Apr 21 2021 Aaron Blasdel <ablasdel@gmail.com> - 0.5.9-1
- Autogenerated by Bloom

* Tue Mar 17 2020 Aaron Blasdel <ablasdel@gmail.com> - 0.5.8-1
- Autogenerated by Bloom

* Tue Mar 17 2020 Aaron Blasdel <ablasdel@gmail.com> - 0.5.7-1
- Autogenerated by Bloom

