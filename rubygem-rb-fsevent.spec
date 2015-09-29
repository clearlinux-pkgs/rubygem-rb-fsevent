Name     : rubygem-rb-fsevent
Version  : 0.9.5
Release  : 2
URL      : https://rubygems.org/downloads/rb-fsevent-0.9.5.gem
Source0  : https://rubygems.org/downloads/rb-fsevent-0.9.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core

%description
[![Code Climate](https://codeclimate.com/badge.png)](https://codeclimate.com/github/thibaudgg/rb-fsevent)
[![endorse](https://api.coderwall.com/ttilley/endorsecount.png)](https://coderwall.com/ttilley)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rb-fsevent-0.9.5
gem spec %{SOURCE0} -l --ruby > rubygem-rb-fsevent.gemspec

%build
gem build rubygem-rb-fsevent.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rb-fsevent-0.9.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rb-fsevent-0.9.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/cdesc-FSEvent.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/open_pipe-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/options_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/parse_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/shellescape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/shellescaped_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/stop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/FSEvent/watch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rb-fsevent-0.9.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/rb-fsevent-0.9.5/
/usr/lib64/ruby/gems/2.2.0/specifications/rb-fsevent-0.9.5.gemspec
