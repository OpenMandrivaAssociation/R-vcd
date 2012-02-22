%bcond_with bootstrap
%global packname  vcd
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2_12
Release:          2
Summary:          Visualizing Categorical Data
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-12.tar.gz
Requires:         R-MASS R-grid R-colorspace R-stats R-utils
Requires:         R-grDevices R-KernSmooth R-mvtnorm R-kernlab
%if %{without bootstrap}
Requires:         R-HSAUR 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-MASS R-grid R-colorspace R-stats R-utils
BuildRequires:    R-grDevices R-KernSmooth R-mvtnorm R-kernlab
%if %{without bootstrap}
BuildRequires:    R-HSAUR 
%endif

%description
Visualization techniques, data sets, summary and inference procedures
aimed particularly at categorical data. Special emphasis is given to
highly extensible grid graphics. The package was inspired by the book
"Visualizing Categorical Data" by Michael Friendly.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
