Summary:	A small collection of X utilities useful when running XMonad
Summary(pl.UTF-8):	Mały zestaw narzędzi dla X przydatnych przy używaniu XMonada
Name:		xmonad-utils
Version:	0.1.3.3
Release:	4
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d0ef4c556313f87c8311afd56a6e4ff9
URL:		http://hackage.haskell.org/package/xmonad-utils/
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-X11 >= 1.3
BuildRequires:	ghc-random >= 1.0
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Requires:	ghc-X11 >= 1.3
Requires:	ghc-random >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

%description
A small collection of X utilities useful when running XMonad. It
includes:
- hxsel, which returns the text currently in the X selection;
- hslock, a simple X screen lock;
- hmanage: an utility to toggle the override-redirect property of any
  window;
- hhp, a simple utility to hide the pointer, similar to unclutter. 

%description -l pl.UTF-8
Mały zestaw narzędzi dla X, przydatnych przy używaniu zarządcy okien
XMonad. Zawiera:
- hxsel - zwracający tekst z aktualnego zaznaczenia X;
- hslock - prosta blokada ekranu X;
- hmanage - narzędzie do przełączania właściwości override-redirect
  dowolnego okna;
- hhp - proste narzędzie do ukrywania wskaźnika, podobne do unclutter.

%prep
%setup -q

%build
runhaskell Setup.lhs configure -v2 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.lhs build

%install
rm -rf $RPM_BUILD_ROOT

runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hhp
%attr(755,root,root) %{_bindir}/hmanage
%attr(755,root,root) %{_bindir}/hslock
%attr(755,root,root) %{_bindir}/hxput
%attr(755,root,root) %{_bindir}/hxsel
