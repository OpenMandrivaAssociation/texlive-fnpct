%global tl_name fnpct
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Manage footnote marks interaction with punctuation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnpct
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpct.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpct.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package moves footnote marks after following punctuation (comma or
full stop), and adjusts kerning as appropriate. As a side effect, a
change to the handling of multiple footnotes is provided.

