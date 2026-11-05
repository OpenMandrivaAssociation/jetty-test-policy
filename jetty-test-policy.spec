%bcond_with javadoc
Name:           jetty-test-policy
Version:        1.2
Release:        10
Summary:        Jetty test policy files


License:        ASL 2.0 or EPL
URL:            https://www.eclipse.org/jetty/
Source0:        https://github.com/jetty/jetty.toolchain/archive/refs/tags/%{name}-%{version}.tar.gz
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
Source2:        https://www.eclipse.org/legal/epl/epl-v10.html
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

Requires:       javapackages-filesystem

%description
Jetty test policy files

%if %{with javadoc}
%package        javadoc
Summary:        API documentation for %{name}

Requires:       javapackages-filesystem

%endif
%if %{with javadoc}
%description    javadoc
%{summary}.


%endif
%prep
%setup -q -n jetty-toolchain-%{name}-%{version}
# No parent checkout. Drop the extra jar executions: sign is gone upstream
# of this plugin, and a second jar goal replaces the main artifact.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r"\s*<parent>.*?</parent>", "", text, count=1, flags=re.S)
text = re.sub(
    r"\s*<plugin>\s*<groupId>org\.apache\.maven\.plugins</groupId>\s*<artifactId>maven-jar-plugin</artifactId>.*?</plugin>",
    "",
    text,
    count=1,
    flags=re.S,
)
head, sep, tail = text.partition("<artifactId>")
if sep and "<groupId>" not in head:
    text = head + "<groupId>org.eclipse.jetty.toolchain</groupId>\n  " + sep + tail
path.write_text(text)
PY
cp -p %{SOURCE2} %{SOURCE3} .

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc epl-v10.html LICENSE-2.0.txt

%endif
