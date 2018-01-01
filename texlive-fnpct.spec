Name:		texlive-fnpct
Version:	0.4e
Release:	1
Summary:	Manage footnote marks' interaction with punctuation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fnpct
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpct.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpct.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package moves footnote marks after following punctuation
(comma or full stop), and adjusts kerning as appropriate. As a
side effect, a change to the handling of multiple footnotes is
provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fnpct
%doc %{_texmfdistdir}/doc/latex/fnpct

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
