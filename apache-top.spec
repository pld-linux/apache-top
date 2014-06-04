Summary:	Povides real-time display of the active processes from a remote apache server
Name:		apache-top
Version:	0.1
# date when fetched from git
Release:	0.20140604.1
License:	GPL v2
Group:		Applications/System
Source0:	https://raw.githubusercontent.com/fr3nd/apache-top/master/%{name}.py
# Source0-md5:	639f12becdbeb1a915b3d982728bf61b
URL:		http://www.fr3nd.net/projects/apache-top/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python >= 1:2.7
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apache-top provides real-time display of the active processes from a
remote apache server. I’ts like the top linux command.

With apache-top you can get:

The active apache processes with their associated PID, the status, the
seconds being active, the CPU usage, the asociated VirtualHost, the
accessing ip and the request (POST or GET, the file being accessed and
the used protocol) The server uptime and the last time it was
restarted The CPU usage Requests by second, Kb by second and the
average Kb by request Number of active and inactive processes A graph
with the inactive and active processes and their status

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apache-top
