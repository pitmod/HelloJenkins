Name:           hellojenkins
Version:        1
Release:        0
Summary:        Just a jenkins with github test

Group:          swissunix
BuildArch:      noarch
License:        GPL
URL:            https://github.com/pitmod/HelloJenkins.git
Source0:        hellojenkins-1.0.tar.gz

%description
Some bloody jenkins description about staff

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/hellojenkins
install -m 0755 hellojenkins.sh $RPM_BUILD_ROOT/etc/hellojenkins/hellojenkins.sh
install -m 0644 README.md $RPM_BUILD_ROOT/etc/hellojenkins/config.txt

%files
/etc/hellojenkins
/etc/hellojenkins/hellojenkins.sh
/etc/hellojenkins/config.txt

%changelog
* Sun Aug 4 2019 Pit 1.0.0
  - Initial rpm release
