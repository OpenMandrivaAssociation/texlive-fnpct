# revision 33144
# category Package
# catalog-ctan /macros/latex/contrib/fnpct
# catalog-date 2014-03-10 13:15:59 +0100
# catalog-license lppl1.3
# catalog-version 0.4b
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
%{_texmfdistdir}/tex/latex/fnpct/fnpct.sty
%doc %{_texmfdistdir}/doc/latex/fnpct/README
%doc %{_texmfdistdir}/doc/latex/fnpct/fnpct_en.pdf
%doc %{_texmfdistdir}/doc/latex/fnpct/fnpct_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
