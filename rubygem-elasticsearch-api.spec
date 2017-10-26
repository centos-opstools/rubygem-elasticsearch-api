# Generated from elasticsearch-api-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch-api

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Ruby API for Elasticsearch
License: ASL 2.0
URL: https://github.com/elasticsearch/elasticsearch-ruby/tree/master/elasticsearch-api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(multi_json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby API for Elasticsearch. See the `elasticsearch` gem for full integration.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%{gem_instdir}/utils
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test

%changelog
* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 2.0.2-1
- version 2.0.2

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 1.0.18-1
- version 1.0.18

* Mon Mar 23 2015 Steve Traylen <steve.traylen@cern.ch> - 1.0.7-1
- Update source 1.0.7

* Fri Aug 08 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0.4-2
- Use correct timestamped source files.

* Thu Jul 03 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0.4-1
- Initial package
