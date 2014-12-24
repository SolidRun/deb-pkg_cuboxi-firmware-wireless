#
# spec file for package cuboxi-firmware-wireless
#
# Copyright (c) 2014 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name: cuboxi-firmware-wireless
Version: 1
Release: 1
License: MIT
Group: System/Kernel
Summary: Wireless firmware files for cubox-i
Source: %{name}-%{version}.tar.gz
Requires: firmware(brcm/brcmfmac4329-sdio.bin)
Requires: firmware(brcm/brcmfmac4329-sdio.txt)
Requires: firmware(brcm/brcmfmac4330-sdio.bin)
Requires: firmware(brcm/brcmfmac4330-sdio.txt)
Requires: firmware(brcm/bcm4329b1.hcd)
Requires: firmware(brcm/bcm4330.hcd)
%description
Provides firmware required by wireless hardware in cubox-i and hummingboard.

%package -n cuboxi-firmware-wifi
Summary: Wifi firmware for cubox-i
#Provides: firmware(brcm/brcmfmac4329-sdio.bin)
#Provides: firmware(brcm/brcmfmac4330-sdio.bin)
%description -n cuboxi-firmware-wifi
Provides wifi firmware for cubox-i and hummingboard.

%package -n cuboxi-firmware-wifi-config
License: Broadcom MIT
Summary: wifi firmware configuration for cubox-i
Requires: firmware(brcm/brcmfmac4329-sdio.bin)
Requires: firmware(brcm/brcmfmac4330-sdio.bin)
%description -n cuboxi-firmware-wifi-config
Provides the required config files for cubox-i and hummingboard wifi firmware.

%package -n cuboxi-firmware-bluetooth
License: Broadcom MIT
Summary: Bluetooth firmware for cubox-i
%description -n cuboxi-firmware-bluetooth
Provides bluetooth firmware for cubox-i and hummingboard.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/lib/firmware/brcm
install -v -m644 brcmfmac4329-sdio.bin %{buildroot}/lib/firmware/brcm/
install -v -m644 brcmfmac4329-sdio.txt %{buildroot}/lib/firmware/brcm/
install -v -m644 brcmfmac4330-sdio.bin %{buildroot}/lib/firmware/brcm/
install -v -m644 brcmfmac4330-sdio.txt %{buildroot}/lib/firmware/brcm/
install -v -m644 bcm4329b1.hcd %{buildroot}/lib/firmware/brcm/
install -v -m644 bcm4330.hcd %{buildroot}/lib/firmware/brcm/

%files -n cuboxi-firmware-wifi
%dir /lib/firmware/brcm
/lib/firmware/brcm/*.bin

%files -n cuboxi-firmware-wifi-config
%dir /lib/firmware/brcm
/lib/firmware/brcm/*.txt

%files -n cuboxi-firmware-bluetooth
%dir /lib/firmware/brcm
/lib/firmware/brcm/*.hcd

%changelog
