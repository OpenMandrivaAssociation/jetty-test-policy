%{?_javapackages_macros:%_javapackages_macros}
Name:           jetty-test-policy
Version:        1.2
Release:        9.0%{?dist}
Summary:        Jetty test policy files


License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
Source2:        http://www.eclipse.org/legal/epl-v10.html
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  jetty-toolchain
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-surefire-provider-junit

Requires:       maven
Requires:       jpackage-utils
Requires:       jetty-toolchain

%description
Jetty test policy files

%package        javadoc
Summary:        API documentation for %{name}

Requires:       jpackage-utils

%description    javadoc
%{summary}.


%prep
%setup -q
cp -p %{SOURCE2} %{SOURCE3} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html LICENSE-2.0.txt

%changelog
* Mon Aug 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-9
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Sep 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-5
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-2
- Added missing BR on surefire-provider-junit

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-1
- Initial version of the package

