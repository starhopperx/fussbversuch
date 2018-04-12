from bs4 import BeautifulSoup
import requests
from lxml import html
import re
import pprint

#r = requests.get('http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G')
#soup = BeautifulSoup(r.content, "html.parser")

html = '''
<!doctype html>
<html class="no-js">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		
		
		<title>B-Junioren Landesliga - Baden – B-Junioren - 2017/2018: Ergebnisse, Tabelle und Spielplan bei FUSSBALL.DE</title>
		<meta name="default_image_title" content=""/>
		<link rel="canonical" href="http://www.fussball.de/spieltag/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" />
		<meta name="description" content="B-Junioren Landesliga 2017/2018 im Baden: Alle Ergebnisse, die Tabelle und der komplette Spielplan der B-Junioren Landesliga der B-Junioren aus dem Landesverband Baden bei FUSSBALL.DE"/>
		<meta name="keywords" content="Begegnungen,B-Junioren Landesliga,Baden,(Meisterschaft),Spieljahr 17/18,Baden"/>
		<meta name="robots" content="NOINDEX"/>
		<meta name="generator" content=""/>
		<meta name="twitter:card" content="summary"/>
		<meta name="twitter:description" content="B-Junioren Landesliga 2017/2018 im Baden: Alle Ergebnisse, die Tabelle und der komplette Spielplan der B-Junioren Landesliga der B-Junioren aus dem Landesverband Baden bei FUSSBALL.DE"/>
		<meta name="twitter:image" content="http://www.fussball.de/export.media/-/action/getSocialMediaImage/page/spieltagsuebersicht/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G"/>
		<meta name="twitter:title" content="B-Junioren Landesliga - Baden – B-Junioren - 2017/2018: Ergebnisse, Tabelle und Spielplan bei FUSSBALL.DE"/>
		<meta property="og:title" content="B-Junioren Landesliga - Baden – B-Junioren - 2017/2018: Ergebnisse, Tabelle und Spielplan bei FUSSBALL.DE"/>
		<meta property="og:image" content="http://www.fussball.de/export.media/-/action/getSocialMediaImage/page/spieltagsuebersicht/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G"/>
		<meta property="og:image:width" content="600"/>
		<meta property="og:image:height" content="315"/>
		<meta property="og:url" content="http://www.fussball.de/spieltag/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G"/>
		<meta property="og:type" content="website"/>
		<meta property="og:description" content="B-Junioren Landesliga 2017/2018 im Baden: Alle Ergebnisse, die Tabelle und der komplette Spielplan der B-Junioren Landesliga der B-Junioren aus dem Landesverband Baden bei FUSSBALL.DE"/>

		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

		<link rel="shortcut icon" type="image/x-icon" href="//www.fussball.de/static/por/6.80.99.3077/icon/favicon.ico" />
        <link rel="apple-touch-icon-precomposed" href="//www.fussball.de/static/por/6.80.99.3077/images/apple-touch-icon-precomposed.png">

		<link rel="stylesheet" href="//www.fussball.de/static/por/6.80.99.3077/css/style.css" />

		<!-- components::script_open_app -->

    <script type="text/javascript" nonce="">
      if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i))) {
        var headTag = document.getElementsByTagName("head")[0];
        var metaTag = document.createElement('meta');
        metaTag.name = 'apple-itunes-app';
        metaTag.content = 'app-id=901148836';
        headTag.appendChild(metaTag);
      }
    </script>

<!-- /components::script_open_app -->


		<script type="text/javascript" nonce="" src="//www.fussball.de/static/por/6.80.99.3077/js/lib/modernizr.min.js"></script>
			
		
		

	
		<script type="text/javascript" src="//assets.adobedtm.com/f1da398c27214bec64e7aa593c5a00f226037c10/satelliteLib-c17ea2874a9aa84b093067b5d761512b57eb0605.js"></script>
<script type="text/javascript">/*<![CDATA[*/(function(l,o,a,d,i,n,g,w,e,b){
g='AccengageWebSDKObject';w='script';l[g]=l[g]||{};l[g][n]=d;
l[d]=l[d]||[];l[d].p={'date':1*new Date(),'window':l,'document':o,'params':a};
e=o.createElement(w);b=o.getElementsByTagName(w)[0];e.async=1;
e.src='https://'+n+i+'/init.js';b.parentNode.insertBefore(e,b);
})(window,document,{},'ACC','/pushweb/assets','fussball-de-by.accengage.net');/*]]>*/</script>
<!-- Steps see adition docs -->
<!-- Step 1. load helper lib -->
<script type="text/javascript" src="http://www.fussball.de/static/por/6.80.99.3077/js/lib/wmConfig.min.js"></script>
<!-- 2. load ad lib -->
<script type="text/javascript">/*<![CDATA[*/var adition = adition || {};adition.srq = adition.srq || [];(function() {var script = document.createElement("script");script.type = "text/javascript";script.src = (document.location.protocol === "https:" ? "https:" : "http:") + "//imagesrv.adition.com/js/srp.js";script.charset = "utf-8";script.async =true;var firstScript = document.getElementsByTagName("script")[0];firstScript.parentNode.insertBefore(script, firstScript);})();/*]]>*/</script>
<!-- 3. register ad farm -->
<script type="text/javascript">/*<![CDATA[*/wmConfig.initConnection();wmConfig.pushViewport();/*]]>*/</script>
<!-- 4. configure slots, load and render -->
<script type="text/javascript">/*<![CDATA[*/if (wmConfig.existsApiLibrary()) {adition.srq.push(function(api) {
api.setProfile('Verband','32');
api.setProfile('Spieltyp','1');
api.setProfile('Spielklasse','146');
api.setProfile('Mannschaftsart','6');
});}/*]]>*/</script>
<script type="text/javascript">/*<![CDATA[*/
wmConfig.pushConfig('slot-3688414',3688414);
wmConfig.loadAndRender();/*]]>*/</script>

		<script type="text/javascript">/*<![CDATA[*/
edArtikelId='';
edArtikelKategorie='';
edArtikelSchluesselwoerter='';
edArtikelTitel='';
edChannel='ligen';
edGastmannschaftId='';
edGastmannschaftName='';
edGebiet='0123456789ABCDEF0123456700004180';
edGebietName='Baden';
edHeimmannschaftId='';
edHeimmannschaftName='';
edMandant='32';
edMannschaftId='';
edMannschaftName='';
edMannschaftsart='230';
edMannschaftsartId='230';
edMannschaftsartName='B-Junioren';
edMannschaftsartTypId='6';
edMannschaftsartTypName='B-Junioren';
edSaison='1718';
edSeite='wettbewerb_aktuell/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G';
edSeitennameKurz='wettbewerb';
edSeitennameLang='wettbewerb_aktuell';
edSpielId='';
edSpielgebietId='0123456789ABCDEF0123456700004180';
edSpielgebietName='Baden';
edSpielklasse='146';
edSpielklasseId='146';
edSpielklasseName='Landesliga';
edSpielklasseTypId='54';
edSpielklasseTypName='Freundschaftsspiele';
edSubchannel='aktuell';
edTickerId='';
edVerbandId='0123456789ABCDEF0123456700004180';
edVerbandName='Baden';
edVereinId='';
edVereinName='';
edVideoId='';
edVideoTitle='';
edWettbewerbId='020EQ1DMQ8000003VS54898DVTQF3A0H-G';
edWettbewerbName='bfv-B-Junioren Landesliga Rhein/Neckar';
edWettbewerbUrl='http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G';
edWettkampfTyp='1';
edWettkampfTypName='Meisterschaften';
edWidgetTyp='';
fbedExtMa='';
fbedExtPlzMultiSpielst='68723+69190+74909+74939';
fbedExtPlzMultiVerein='68723+69190+74909+74939';
fbedExtPlzSpielst='';
fbedExtPlzVerein='';
fbedTeamTypeName='B-Junioren';
fbedWidgetKey='';
trackingcountername='spieltagsuebersicht.17/18.Baden.Meisterschaften.B-Junioren.Landesliga.Baden.01VPN9BKNO000000VS54898DVT75CK91-C';
if (window.location.href.indexOf('#_=_') > 0) {
	window.location = window.location.href.replace(/#.*/, '');
}
/*]]>*/</script>


	</head>
	<body class="fbde" data-ng-controller="ApplicationController" data-marketing-cookies data-click-tracking data-scroll-spy data-ng-cloak global-events data-obfuscation-stylesheet="//www.fussball.de/export.fontface/-/id/%ID%/type/css">
		<header data-ng-controller="FlyoutController" data-ng-class="{active:flyoutState.isOpen, 'active-layer':layerState.isOpen}">
	<nav class="header-meta-nav">
		<div class="container">
			<div class="metanav-left">
				<ul>
					<li>
						<a href="http://www.dfb.de" target="_blank">dfb.de</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://kampagne.dfb.de/unsere-amateure/" target="_blank">Amateurfußballkampagne</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://fanshop.dfb.de/" target="_blank">DFB-Fanshop</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://fanclub.dfb.de/index.php?id=2" target="_blank">Fan Club Nationalmannschaft</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate" target="_blank">Shop</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.dfb.de/tickets" target="_blank">Tickets</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/partner" target="_blank">Partner</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/" target="_blank">FAQ</a>
					</li>
				</ul>
				<div class="sponsor-text">FUSSBALL.DE wird präsentiert von</div>
			</div>
			<div class="metanav-right">
				<div class="sponsor">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/temp/sponsor.png">
					</a>
				</div>
				<a href="#!" id="editor-link" class="visible-full">
					<span>Link</span>
					<script type="text/javascript">document.addEventListener('DOMContentLoaded', function () {document.getElementById('editor-link').addEventListener('click', function doThings() { alert('/spieltagsuebersicht/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G');});});</script>
					<div data-user-dependency="{'FBDE_COMMUNITY_IN':'equal'}" data-ajaxcontent-type="jsonp" data-user="{'FBDE_COMMUNITY_IN':'1'}" data-ajaxcontent="https://www.fussball.de/login.community"></div>
					<div data-user-dependency="{'FBDE_COMMUNITY_OUT':'equal'}" data-ajaxcontent-type="jsonp" data-user="{'FBDE_COMMUNITY_OUT':'1'}" data-ajaxcontent="https://www.fussball.de/logout.community"></div>
				</a>
			</div>
		</div>
	</nav>
	<div class="header-main-nav">
		<div class="container">
			<div class="logo-wrapper">
				<div id="logo">
					<a data-ng-click="onLogoClick($event)" href="http://www.fussball.de/homepage">
						<img src="http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/logo.svg" alt="logo" width="24" class="logo-graphic" height="16">
						<span class="logo-letters">fussball.de</span>
					</a>
				</div>
			</div>
			<nav class="secondary-nav">
				<ul>
					<li class="seondary-nav-toggle">
						<a data-ng-click="toggleVisibleMobile()"><span class="icon-toggle"></span></a>
					</li>
					<li>
						<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
							<div data-flyoutitem-identifier="#login">
								
								<span></span>
								<img data-user-interpolate="src" data-user-interpolate-tmpl="%FBDE_USER_THUMB%" alt="thumb" class="img-profile">
							</div>
						</div>
						<div data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">
							<a href="https://www.fussball.de/login?fw_url=http%3A%2F%2Fwww.fussball.de%2Fspieltagsuebersicht%2Fbfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden%2F-%2Fstaffel%2F020EQ1DMQ8000003VS54898DVTQF3A0H-G"><span class="icon-login"></span></a>
						</div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#search"><span class="icon-search"></span></div>
					</li>
				</ul>
			</nav>
			<nav data-ng-class="{active: isVisibleMobile, hidden: scopeEnv.isMainMenuHidden}" class="primary-nav">
				<ul class="fast">
					<li>
						<a href="https://www.fussball.de/favorites"><span class="icon-favorits"></span>Favoriten</a>
					</li>
					<li>
						<a href="http://www.fussball.de/matchkalender"><span class="icon-matchcal"></span>Matchkalender</a>
					</li>
					<li>
						<div data-flyoutnavitem="main">
							<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-flyoutitem-identifier="#login">
								
								<span></span>
								<img data-user-interpolate="src" data-user-interpolate-tmpl="%FBDE_USER_THUMB%" alt="thumb" class="img-profile">
								<span data-user-interpolate="innerHTML" data-user-interpolate-tmpl="%FBDE_NICKNAME%"></span>
							</div>
						</div>
						<div data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">
							<a href="https://www.fussball.de/login?fw_url=http%3A%2F%2Fwww.fussball.de%2Fspieltagsuebersicht%2Fbfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden%2F-%2Fstaffel%2F020EQ1DMQ8000003VS54898DVTQF3A0H-G"><span class="icon-login"></span>Anmelden</a>
						</div>
					</li>
					<li data-flyoutnavitem="main">
						<div data-flyoutitem-identifier="#search"><span></span>Suche<span class="icon-search"></span></div>
					</li>
				</ul>
				<ul class="main">
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#flyout-news">News<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}" class="active">
						<div data-flyoutitem-identifier="#competitions">Ligen<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#pros">Vereine & Verbände<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#trainings">Training & Service<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#tv">Videos & Foren<span class="icon-angle-right"></span></div>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate/" target="_blank">Shop<span class="icon-angle-right"></span></a>
					</li>
				</ul>
				<ul class="meta">
					<li>
						<a href="http://www.dfb.de" target="_blank">dfb.de<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://kampagne.dfb.de/unsere-amateure/" target="_blank">Amateurfußballkampagne<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://fanshop.dfb.de/" target="_blank">DFB-Fanshop<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://fanclub.dfb.de/index.php?id=2" target="_blank">Fan Club Nationalmannschaft<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate" target="_blank">Shop<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://www.dfb.de/tickets" target="_blank">Tickets<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://www.fussball.de/partner" target="_blank">Partner<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/" target="_blank">FAQ<span class="icon-link-arrow"></span></a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
	<div data-user-favorites-load-cookie="FBDE_USER_ID" data-ng-class="{'opened':flyoutState.isOpen}" id="header-flyout" class="header-flyout" data-user-favorites-load="https://www.fussball.de/ajax.favorites">
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="flyout-news" class="flyout-subnav">
			<div class="container">
				<div data-ng-controller="ToolboxController" class="news-list-toolbox news-list-toolbox-menu" data-toolbox>
					<div class="flyout-left">
						<nav class="flyout-nav">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>News</h4>
							<ul>
								<li data-toolbox-value="all_news" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/all_news">
									<div><span></span>Alle<span></span></div>
								</li>
								<li data-toolbox-value="magazin" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/magazin">
									<div><span></span>Magazin<span></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="regional-league-categories">
									<div data-flyoutitem-identifier="#regional-league-categories"><span></span>Regionalliga<span class="icon-angle-right"></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="association-categories">
									<div data-flyoutitem-identifier="#association-categories"><span></span>Verbände<span class="icon-angle-right"></span></div>
								</li>
								<li data-toolbox-value="service" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/service">
									<div><span></span>Service<span></span></div>
								</li>
								<li data-toolbox-value="aktionen" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/aktionen">
									<div><span></span>Aktionen<span></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="helpcenter-categories">
									<div data-flyoutitem-identifier="#helpcenter-categories"><span></span>Hilfe-Center<span class="icon-angle-right"></span></div>
								</li>
							</ul>
						</nav>
					</div>
					<div class="flyout-right">
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="helpcenter-categories" class="flyout-tab">
							<div data-flyout-content=".filter-helpcenter" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-helpcenter-categories" data-toolbox-key="helpcenter-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Hilfe-Center<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/helpcenter" data-toolbox-key="helpcenter-categories" class="filter-categories filter-assoc filter-helpcenter">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Hilfe-Center
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11198">
													<strong>Allgemeines</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11199">
													<strong>APP</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11200">
													<strong>Liveticker</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11201">
													<strong>Mannschaftsseite</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11202">
													<strong>Profile</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11203">
													<strong>Registrierung</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11204">
													<strong>Training & Service</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11205">
													<strong>Widgets</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="regional-league-categories" class="flyout-tab">
							<div data-flyout-content=".filter-regionalliga" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-regional-league-categories" data-toolbox-key="regional-league-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Regionalliga<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/regionalliga" data-toolbox-key="regional-league-categories" class="filter-categories filter-assoc filter-regionalliga">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Regionalligen
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11212">
													<strong>Regionalliga Nord</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11213">
													<strong>Regionalliga Nordost</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11211">
													<strong>Regionalliga West</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11209">
													<strong>Regionalliga Südwest</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11210">
													<strong>Regionalliga Bayern</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="association-categories" class="flyout-tab">
							<div data-flyout-content=".filter-verband" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-association-categories" data-toolbox-key="association-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Verbände<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/verbaende" data-toolbox-key="association-categories" class="filter-categories filter-assoc filter-verband">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Verbände
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11032">
													<div class="logo hidden-small"><span data-alt="Baden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004180"></span></div>
													<strong>Baden</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11031">
													<div class="logo hidden-small"><span data-alt="Bayern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/00ES8GNCQK000000VV0AG08LVUPGND5I"></span></div>
													<strong>Bayern</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11066">
													<div class="logo hidden-small"><span data-alt="Berlin" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004240"></span></div>
													<strong>Berlin</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11061">
													<div class="logo hidden-small"><span data-alt="Brandenburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004250"></span></div>
													<strong>Brandenburg</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11002">
													<div class="logo hidden-small"><span data-alt="Bremen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004090"></span></div>
													<strong>Bremen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11003">
													<div class="logo hidden-small"><span data-alt="Hamburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004080"></span></div>
													<strong>Hamburg</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11034">
													<div class="logo hidden-small"><span data-alt="Hessen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004170"></span></div>
													<strong>Hessen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11062">
													<div class="logo hidden-small"><span data-alt="Mecklenburg-Vorpommern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004220"></span></div>
													<strong>Mecklenburg-Vorpommern</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11023">
													<div class="logo hidden-small"><span data-alt="Mittelrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004120"></span></div>
													<strong>Mittelrhein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11022">
													<div class="logo hidden-small"><span data-alt="Niederrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004110"></span></div>
													<strong>Niederrhein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11001">
													<div class="logo hidden-small"><span data-alt="Niedersachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004100"></span></div>
													<strong>Niedersachsen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11041">
													<div class="logo hidden-small"><span data-alt="Rheinland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004140"></span></div>
													<strong>Rheinland</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11043">
													<div class="logo hidden-small"><span data-alt="Saarland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004150"></span></div>
													<strong>Saarland</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11063">
													<div class="logo hidden-small"><span data-alt="Sachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004270"></span></div>
													<strong>Sachsen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11064">
													<div class="logo hidden-small"><span data-alt="Sachsen-Anhalt" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004230"></span></div>
													<strong>Sachsen-Anhalt</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11004">
													<div class="logo hidden-small"><span data-alt="Schleswig-Holstein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004070"></span></div>
													<strong>Schleswig-Holstein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11033">
													<div class="logo hidden-small"><span data-alt="Südbaden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004190"></span></div>
													<strong>Südbaden</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11042">
													<div class="logo hidden-small"><span data-alt="Südwest" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004160"></span></div>
													<strong>Südwest</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11065">
													<div class="logo hidden-small"><span data-alt="Thüringen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004260"></span></div>
													<strong>Thüringen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11021">
													<div class="logo hidden-small"><span data-alt="Westfalen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004130"></span></div>
													<strong>Westfalen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11035">
													<div class="logo hidden-small"><span data-alt="Württemberg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004200"></span></div>
													<strong>Württemberg</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="competitions" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Ligen</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#wam"><span></span>Alle Ligen<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#topleagues"><span></span>Top-Ligen<span class="icon-angle-right"></span></div>
							</li>
							<li data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-ng-class="{'current':isCurrent}">
								<a href="https://www.fussball.de/account.matchplan.next">Dein Spielplan</a>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#stats"><span></span>Amateurstatistiken<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#matchcal"><span></span>Matchkalender<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="wam" class="flyout-tab">
						<div class="wam header-flyout-wam">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Wettbewerbsauswahl</h4>
							<div class="inner">
								<form method="GET" data-url-submit="" data-url-competitions="//www.fussball.de/wam_wettbewerbsurls_CLIENT_SEASON_COMPETITIONTYPE_TEAMTYPE.json" data-url-base="//www.fussball.de/wam_base.json" data-url-areas="//www.fussball.de/wam_arten_CLIENT_SEASON_COMPETITIONTYPE.json" data-wam>
									<div class="form-wrapper">
										<div data-ng-class="{on: wamData.clients.isOpen, cta: wamData.clients.isCta, disabled: wamData.clients.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.clients.length == 1 || clickHandler(0)" class="selection">
												<div data-ng-bind="wamData.clientsSelected.label || 'Verband wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.clients" data-ng-class="{on: wamData.clientsSelected.id == option.id}">
													<a data-ng-click="wamData.clients.isOpen = !wamData.clients.isOpen; wamData.clientsSelected = option; wamUpdate('clients',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.clientsSelected" size="1" data-ng-disabled="wamData.clients.length == 1" name="clients" data-ng-change="onChange()" data-label="Verband wählen" data-ng-options="option as option.label for option in wamData.clients track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.seasons.isOpen, cta: wamData.seasons.isCta, disabled: wamData.seasons.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.seasons.length == 1 || clickHandler(1)" class="selection">
												<div data-ng-bind="wamData.seasonsSelected.label || 'Saison wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.seasons" data-ng-class="{on: wamData.seasonsSelected.id == option.id}">
													<a data-ng-click="wamData.seasons.isOpen = !wamData.seasons.isOpen; wamData.seasonsSelected = option; wamUpdate('seasons',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.seasonsSelected" size="1" data-ng-disabled="wamData.seasons.length == 1" name="seasons" data-ng-change="onChange()" data-label="Saison wählen" data-ng-options="option as option.label for option in wamData.seasons track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.competitionTypes.isOpen, cta: wamData.competitionTypes.isCta, disabled: wamData.competitionTypes.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.competitionTypes.length == 1 || clickHandler(2)" class="selection">
												<div data-ng-bind="wamData.competitionTypesSelected.label || 'Typ wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.competitionTypes" data-ng-class="{on: wamData.competitionTypesSelected.id == option.id}">
													<a data-ng-click="wamData.competitionTypes.isOpen = !wamData.competitionTypes.isOpen; wamData.competitionTypesSelected = option; wamUpdate('competitionTypes',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.competitionTypesSelected" size="1" data-ng-disabled="wamData.competitionTypes.length == 1" name="competitionTypes" data-ng-change="onChange()" data-label="Typ wählen" data-ng-options="option as option.label for option in wamData.competitionTypes track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.teamTypes.isOpen, cta: wamData.teamTypes.isCta, disabled: wamData.teamTypes.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.teamTypes.length == 1 || clickHandler(3)" class="selection">
												<div data-ng-bind="wamData.teamTypesSelected.label || 'Mannschaftsart wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.teamTypes" data-ng-class="{on: wamData.teamTypesSelected.id == option.id}">
													<a data-ng-click="wamData.teamTypes.isOpen = !wamData.teamTypes.isOpen; wamData.teamTypesSelected = option; wamUpdate('teamTypes',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.teamTypesSelected" size="1" data-ng-disabled="wamData.teamTypes.length == 1" name="teamTypes" data-ng-change="onChange()" data-label="Mannschaftsart wählen" data-ng-options="option as option.label for option in wamData.teamTypes track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.leagues.isOpen, cta: wamData.leagues.isCta, disabled: wamData.leagues.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.leagues.length == 1 || clickHandler(4)" class="selection">
												<div data-ng-bind="wamData.leaguesSelected.label || 'Spielklasse wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.leagues" data-ng-class="{on: wamData.leaguesSelected.id == option.id}">
													<a data-ng-click="wamData.leagues.isOpen = !wamData.leagues.isOpen; wamData.leaguesSelected = option; wamUpdate('leagues',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.leaguesSelected" size="1" data-ng-disabled="wamData.leagues.length == 1" name="leagues" data-ng-change="onChange()" data-label="Spielklasse wählen" data-ng-options="option as option.label for option in wamData.leagues track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.areas.isOpen, cta: wamData.areas.isCta, disabled: wamData.areas.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.areas.length == 1 || clickHandler(5)" class="selection">
												<div data-ng-bind="wamData.areasSelected.label || 'Gebiet wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.areas" data-ng-class="{on: wamData.areasSelected.id == option.id}">
													<a data-ng-click="wamData.areas.isOpen = !wamData.areas.isOpen; wamData.areasSelected = option; wamUpdate('areas',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.areasSelected" size="1" data-ng-disabled="wamData.areas.length == 1" name="areas" data-ng-change="onChange()" data-label="Gebiet wählen" data-ng-options="option as option.label for option in wamData.areas track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.competitions.isOpen, cta: wamData.competitions.isCta, disabled: wamData.competitions.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.competitions.length == 1 || clickHandler(6)" class="selection">
												<div data-ng-bind="wamData.competitionsSelected.label || 'Wettbewerb wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.competitions" data-ng-class="{on: wamData.competitionsSelected.id == option.id}">
													<a data-ng-click="wamData.competitions.isOpen = !wamData.competitions.isOpen; wamData.competitionsSelected = option; wamUpdate('competitions',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.competitionsSelected" size="1" data-ng-disabled="wamData.competitions.length == 1" name="competitions" data-ng-change="onChange()" data-label="Wettbewerb wählen" data-ng-options="option as option.label for option in wamData.competitions track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
									</div>
									<div data-user-favorites-save="https://www.fussball.de/add.favorite">
										<a data-user-dependency="{'FBDE_USER_ID':'exist'}" data-ng-click="saveFavorite(wamData.competitionsSelected)" data-ng-class="{'disabled':!wamData.competitionsSelected.id}" class="button button-primary favorits trigger-login-layer">als Favorit speichern</a>
									</div>
									<div class="form-submit" data-wam-submit>
										<button data-ng-click="submitForm()" data-ng-class="{'disabled':!wamData.competitionsSelected.id}" type="submit" class="button button-primary">Anzeigen</button>
									</div>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="competitions" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="topleagues" class="flyout-tab">
						<div class="header-flyout-wam header-flyout-link-list wam">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Top-Ligen Herren 17/18</h4>
							<div class="inner">
								<h3 class="hidden-small">Herren 17/18</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/bundesliga-deutschland-bundesliga-herren-saison1718-deutschland/-/staffel/01VM7AT5SK000001VS54898EVSV90M3P-G" class="link">Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2bundesliga-deutschland-2bundesliga-herren-saison1718-deutschland/-/staffel/01VV7REICS00000DVS54898DVTPALDN0-G" class="link">2.Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/3liga-deutschland-3liga-herren-saison1718-deutschland/-/staffel/01VM7AUE1K000000VS54898EVSV90M3P-G" class="link">3.Liga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-nord-region-norddeutschland-regionalliga-herren-saison1718-region-norddeutschland/-/staffel/01VON662IK000000VS54898DVT75CK91-G" class="link">Regionalliga Nord<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-nordost-region-nordostdeutschland-regionalliga-herren-saison1718-region-nordostdeutschland/-/staffel/0204BP0IA8000004VS54898EVSIMIKOR-G" class="link">Regionalliga Nordost<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-suedwest-region-suedwestdeutschland-regionalliga-herren-saison1718-region-suedwestdeutschland/-/staffel/0201G63B98000001VS54898EVSIMIKOR-G" class="link">Regionalliga Südwest<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-west-region-westdeutschland-regionalliga-herren-saison1718-region-westdeutschland/-/staffel/01VVHJ6FSG00000AVS54898DVUL01S6C-G" class="link">Regionalliga West<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-bayern-bayern-regionalliga-bayern-herren-saison1718-bayern/-/staffel/0200TN5NS0000007VS54898DVUL01S6C-G" class="link">Regionalliga Bayern<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/dfb-pokal-deutschland-dfb-pokal-herren-saison1718-deutschland/-/staffel/01VUJJCMU4000000VS54898DVTPALDN0-C" class="link">DFB-Pokal<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
						<div class="header-flyout-wam header-flyout-link-list profiles">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Top-Ligen Frauen 17/18</h4>
							<div class="inner">
								<h3 class="hidden-small">Frauen 17/18</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/allianz-frauen-bundesliga-deutschland-bundesliga-frauen-saison1718-deutschland/-/staffel/020C461154000001VS54898EVVNLA7IG-G" class="link">Allianz Frauen-Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2-frauen-bundesliga-nord-deutschland-2bundesliga-frauen-saison1718-deutschland/-/staffel/01VM7B7SQC000002VS54898EVSV90M3P-G" class="link">2. Frauen-Bundesliga Nord<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2-frauen-bundesliga-sued-deutschland-2bundesliga-frauen-saison1718-deutschland/-/staffel/01VM7B7T4C000006VS54898EVSV90M3P-G" class="link">2. Frauen-Bundesliga Süd<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/dfb-pokal-frauen-deutschland-dfb-pokal-frauen-saison1718-deutschland/-/staffel/020A3KANFG000000VS54898DVUVCCN5J-C" class="link">DFB-Pokal Frauen<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="matchcal" class="flyout-tab">
						<div class="matchcal header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Matchkalender</h4>
							<div class="inner form-dark">
								<h3>Begegnungen in deiner Nähe</h3>
								<form method="GET" action="//www.fussball.de/matchkalender" data-rest-form>
									<div data-ng-controller="TypeaheadController" data-typeahead="http://www.fussball.de/public.service/-/action/getPostalCodeCompletions" data-typeahead-minlength="3" data-typeahead-key="plz" class="label-wrapper location" data-typeahead-type="noselect" data-typeahead-default="{'action':'getPostalCodeCompletions'}">
										<div class="typeahead-wrapper">
											<label for="matchplan-calendar-location">Umgebung:</label>
											<input data-ng-model="typeaheadInput.text" name="plz" data-ng-change="updateInput()" data-ng-show="!showSelected()" placeholder="PLZ / Ort*" id="matchplan-calendar-location" type="text" value="" data-ajaxmodel="plz">
											<ul data-ng-class="{'on':isActiveList()}" class="typeahead-list">
												<li data-ng-show="isActiveError()"><span>Keine Postleitzahlen gefunden. Bitte überprüfe deine Angabe.</span></li>
												<li data-ng-repeat="item in filterResults('$', typeaheadItems, typeaheadInput.text)" data-ng-class-even="'even'" data-ng-show="isActiveResults()">
													<a data-ng-click="chooseItem(item, 'postalCode')" href="">{{item.postalCode}}, {{item.city}}</a>
												</li>
											</ul>
											<p data-ng-show="showSelected()" class="typeahead-selected">
												{{typeaheadInput.text}}
												<a data-ng-click="resetSelected()" href="" class="close"><span class="icon-close"></span></a>
											</p>
										</div>
									</div>
									<div class="cal-group">
										<div class="datepicker-wrapper">
											<div data-calendar-type="from" data-calendar-span="14" data-ng-controller="MatchcalController" class="date datepicker label-wrapper">
												<label for="matchcal-date-from">Von:</label>
												<input data-ng-model="dt" data-ng-init="dt='2018-04-11'" name="datum-von" data-datepicker-popup="dd.MM.yyyy" data-is-open="opened" placeholder="Datum*" id="matchcal-date-from" type="text" value="" data-ajaxmodel="datum-von">
												<label for="matchcal-date-from" data-ng-class="{'open':opened}"><span class="icon-matchcal"></span></label>
											</div>
										</div>
										<div class="datepicker-wrapper">
											<div data-calendar-type="to" data-calendar-span="14" data-ng-controller="MatchcalController" class="date datepicker label-wrapper">
												<label for="matchcal-date-to">Bis:</label>
												<input data-ng-model="dt" data-ng-init="dt='2018-04-25'" name="datum-bis" data-datepicker-popup="dd.MM.yyyy" data-is-open="opened" placeholder="Datum*" id="matchcal-date-to" type="text" value="" data-ajaxmodel="datum-bis">
												<label for="matchcal-date-to" data-ng-class="{'open':opened}"><span class="icon-matchcal"></span></label>
											</div>
										</div>
									</div>
									<div data-ng-model="filterCompetitions" data-select-box="single" data-select-box-default="0" data-select-title="Wettbewerbe" class="select-wrapper" data-ajaxmodel="wettkampftyp">
										<select size="1" name="wettkampftyp">
											<option value="-1">Alle</option>
											<option value="1">Meisterschaften</option>
											<option value="8">Pokale</option>
											<option value="3">Turniere</option>
											<option value="7">Freundschaftsspiele</option>
											<option value="6">Privatspiele</option>
											<option value="9">Auswahlspiele</option>
											<option value="11">Futsal-Ligabetrieb</option>
											<option value="2">Hallenturniere (Futsal)</option>
										</select>
									</div>
									<div data-ng-model="filterTeams" data-select-box="multiple" data-select-box-default="0" data-select-title="Mannschaften" class="select-wrapper" data-ajaxmodel="mannschaftsart" data-select-box-multiple="ausgewählt">
										<select size="1" name="mannschaftsart" multiple>
											<option value="-1">Alle</option>
											<option value="1">Herren</option>
											<option value="39">Herren-Reserve</option>
											<option value="54">Herren - Behindertenfußball</option>
											<option value="807">Senioren Ü60 Freizeit/Betrieb</option>
											<option value="809">Senioren Ü50 Freizeit/Betrieb</option>
											<option value="811">Senioren Ü40 Freizeit/Betrieb</option>
											<option value="812">Senioren Ü32 Freizeit/Betrieb</option>
											<option value="813">Herren Freizeit/Betrieb</option>
											<option value="3">A-Junioren</option>
											<option value="6">B-Junioren</option>
											<option value="8">C-Junioren</option>
											<option value="10">D-Junioren</option>
											<option value="12">E-Junioren</option>
											<option value="14">F-Junioren</option>
											<option value="16">G-Junioren</option>
											<option value="19">Altherren</option>
											<option value="20">Alt-Senioren</option>
											<option value="21">Alte Herren Ü50</option>
											<option value="24">Altliga Ü50</option>
											<option value="23">Altliga Ü60</option>
											<option value="47">Alte Herren Ü60</option>
											<option value="49">Altliga Ü70</option>
											<option value="55">Seniorinnen Ü35</option>
											<option value="48">Seniorinnen Ü30</option>
											<option value="4">Frauen</option>
											<option value="5">A-Juniorinnen</option>
											<option value="7">B-Juniorinnen</option>
											<option value="9">C-Juniorinnen</option>
											<option value="11">D-Juniorinnen</option>
											<option value="13">E-Juniorinnen</option>
											<option value="15">F-Juniorinnen</option>
											<option value="17">G-Juniorinnen</option>
											<option value="22">Freizeitsport</option>
											<option value="40">Freizeitsport Frauen</option>
										</select>
									</div>
									<button type="submit" class="button button-primary button-block">Suchen</button>
									<p class="mandatory">* Pflichtfelder</p>
								</form>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="stats" class="flyout-tab">
						<div class="stats header-flyout-stats">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Amateurstatistiken</h4>
							<div class="inner">
								<h3>Deutschlands Beste</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/stats.amateur.team/-/mandantspez/false/stats/4"><span class="icon-team-logo"></span><span class="link">Bestes Team<span class="icon-link-arrow"></span></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/stats.amateur.player/-/mandantspez/false/stats/8"><span class="icon-player-image"></span><span class="link">Bester Stürmer<span class="icon-link-arrow"></span></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/stats.amateur.team/-/mandantspez/false/stats/5"><span class="icon-soccer-ball"></span><span class="link">Alle Top-Statistiken<span class="icon-link-arrow"></span></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="pros" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Vereine & Verbände</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#region"><span></span>Regionalverbände<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#fed"><span></span>Landesverbände<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#searchAssociation"><span></span>Vereine<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#searchPlayer"><span></span>Spieler<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="region" class="flyout-tab">
						<div class="region header-flyout-associations">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Regionalverbände</h4>
							<div class="inner">
								<div class="block">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/regionalverband/region-norddeutschland/-/verband/0123456789ABCDEF0123456700004020" class="association-wrapper">
												<div class="logo"><span data-alt="Region Norddeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004020"></span></div>
												<div class="name">Norddeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-nordostdeutschland/-/verband/0123456789ABCDEF0123456700004060" class="association-wrapper">
												<div class="logo"><span data-alt="Region Nordostdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004060"></span></div>
												<div class="name">Nordostdeutscher Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-sueddeutschland/-/verband/0123456789ABCDEF0123456700004050" class="association-wrapper">
												<div class="logo"><span data-alt="Region Süddeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004050"></span></div>
												<div class="name">Süddeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
								<div class="block last">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/regionalverband/region-suedwestdeutschland/-/verband/0123456789ABCDEF0123456700004040" class="association-wrapper">
												<div class="logo"><span data-alt="Region Südwestdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004040"></span></div>
												<div class="name">Fußball-Regional-Verband Südwest<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-westdeutschland/-/verband/0123456789ABCDEF0123456700004030" class="association-wrapper">
												<div class="logo"><span data-alt="Region Westdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004030"></span></div>
												<div class="name">Westdeutscher Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="fed" class="flyout-tab">
						<div class="fed header-flyout-associations">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Landesverbände</h4>
							<div class="inner">
								<div class="block">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180" class="association-wrapper">
												<div class="logo"><span data-alt="Baden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004180"></span></div>
												<div class="name">Badischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/bremen/-/verband/0123456789ABCDEF0123456700004090" class="association-wrapper">
												<div class="logo"><span data-alt="Bremen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004090"></span></div>
												<div class="name">Bremer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/mittelrhein/-/verband/0123456789ABCDEF0123456700004120" class="association-wrapper">
												<div class="logo"><span data-alt="Mittelrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004120"></span></div>
												<div class="name">Fußball-Verband Mittelrhein<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/saarland/-/verband/0123456789ABCDEF0123456700004150" class="association-wrapper">
												<div class="logo"><span data-alt="Saarland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004150"></span></div>
												<div class="name">Saarländischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/suedbaden/-/verband/0123456789ABCDEF0123456700004190" class="association-wrapper">
												<div class="logo"><span data-alt="Südbaden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004190"></span></div>
												<div class="name">Südbadischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/wuerttemberg/-/verband/0123456789ABCDEF0123456700004200" class="association-wrapper">
												<div class="logo"><span data-alt="Württemberg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004200"></span></div>
												<div class="name">Württembergischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
									<ul class="col last">
										<li>
											<a href="http://www.fussball.de/verband/bayern/-/verband/00ES8GNCQK000000VV0AG08LVUPGND5I" class="association-wrapper">
												<div class="logo"><span data-alt="Bayern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/00ES8GNCQK000000VV0AG08LVUPGND5I"></span></div>
												<div class="name">Bayerischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/hamburg/-/verband/0123456789ABCDEF0123456700004080" class="association-wrapper">
												<div class="logo"><span data-alt="Hamburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004080"></span></div>
												<div class="name">Hamburger Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/niederrhein/-/verband/0123456789ABCDEF0123456700004110" class="association-wrapper">
												<div class="logo"><span data-alt="Niederrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004110"></span></div>
												<div class="name">Fußballverband Niederrhein e.V.<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/sachsen/-/verband/0123456789ABCDEF0123456700004270" class="association-wrapper">
												<div class="logo"><span data-alt="Sachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004270"></span></div>
												<div class="name">Sächsischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/suedwest/-/verband/0123456789ABCDEF0123456700004160" class="association-wrapper">
												<div class="logo"><span data-alt="Südwest" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004160"></span></div>
												<div class="name">Südwestdeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
								<div class="block last">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/verband/berlin/-/verband/0123456789ABCDEF0123456700004240" class="association-wrapper">
												<div class="logo"><span data-alt="Berlin" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004240"></span></div>
												<div class="name">Berliner Fußball-Verband e. V.<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/hessen/-/verband/0123456789ABCDEF0123456700004170" class="association-wrapper">
												<div class="logo"><span data-alt="Hessen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004170"></span></div>
												<div class="name">Hessischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/niedersachsen/-/verband/0123456789ABCDEF0123456700004100" class="association-wrapper">
												<div class="logo"><span data-alt="Niedersachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004100"></span></div>
												<div class="name">Niedersächsischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/sachsen-anhalt/-/verband/0123456789ABCDEF0123456700004230" class="association-wrapper">
												<div class="logo"><span data-alt="Sachsen-Anhalt" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004230"></span></div>
												<div class="name">Fußballverband Sachsen-Anhalt<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/thueringen/-/verband/0123456789ABCDEF0123456700004260" class="association-wrapper">
												<div class="logo"><span data-alt="Thüringen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004260"></span></div>
												<div class="name">Thüringer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
									<ul class="col last">
										<li>
											<a href="http://www.fussball.de/verband/brandenburg/-/verband/0123456789ABCDEF0123456700004250" class="association-wrapper">
												<div class="logo"><span data-alt="Brandenburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004250"></span></div>
												<div class="name">Fußball-Landesverband Brandenburg<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/mecklenburg-vorpommern/-/verband/0123456789ABCDEF0123456700004220" class="association-wrapper">
												<div class="logo"><span data-alt="Mecklenburg-Vorpommern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004220"></span></div>
												<div class="name">Landesfußballverband Mecklenburg-Vorpommern<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/rheinland/-/verband/0123456789ABCDEF0123456700004140" class="association-wrapper">
												<div class="logo"><span data-alt="Rheinland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004140"></span></div>
												<div class="name">Fußballverband Rheinland<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/schleswig-holstein/-/verband/0123456789ABCDEF0123456700004070" class="association-wrapper">
												<div class="logo"><span data-alt="Schleswig-Holstein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004070"></span></div>
												<div class="name">Schleswig-Holsteinischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/westfalen/-/verband/0123456789ABCDEF0123456700004130" class="association-wrapper">
												<div class="logo"><span data-alt="Westfalen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004130"></span></div>
												<div class="name">Fußball- u. Leichtathletik-Verband Westfalen<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="searchAssociation" class="flyout-tab">
						<div class="search header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Vereine</h4>
							<div class="inner form-dark">
								<h3>Vereine nach Name und Region finden</h3>
								<form method="GET" action="//www.fussball.de/suche.verein" data-rest-form>
									<input data-ng-model="text" name="text" placeholder="Vereinsname*" type="text" value="">
									<div class="location label-wrapper">
										<label for="plz">Umgebung</label>
										<input data-ng-model="plz" name="plz" placeholder="PLZ / Ort*" id="flyout-search-club-zip" type="text" value="">
									</div>
									<button type="submit" class="button button-primary button-block">Finden</button>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="club" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="searchPlayer" class="flyout-tab">
						<div class="search header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Spieler</h4>
							<div class="inner form-dark">
								<h3>Spieler nach Name und Region finden</h3>
								<form method="GET" action="//www.fussball.de/suche.spieler" data-rest-form>
									<input data-ng-model="firstname" name="firstname" placeholder="Vorname*" type="text" value="" class="small">
									<input data-ng-model="lastname" name="lastname" placeholder="Nachname*" type="text" value="" class="small">
									<div class="location label-wrapper">
										<label for="plz">Umgebung</label>
										<input data-ng-model="plz" name="plz" placeholder="PLZ / Ort*" id="flyout-search-player-zip" type="text" value="" class="small">
									</div>
									<button type="submit" class="button button-primary button-block">Finden</button>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="player" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="trainings" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Training & Service</h4>
						<ul>
							<li data-ng-class="{'current':isCurrent}">
								<div>
									<a href="http://training-service.fussball.de/">Übersichtsseite<span></span></a>
								</div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings2">Trainer/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings3">Spieler/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings4">Lehrer/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings5">Schiedsrichter/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings6">Vereinsmitarbeiter/in<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings2" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Trainer/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/trainer" class="link">Startseite Trainer/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/bambini" class="link">Bambini<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/f-juniorin" class="link">F-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/e-juniorin" class="link">E-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/d-juniorin" class="link">D-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/c-juniorin" class="link">C-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/b-juniorin" class="link">B-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/a-juniorin" class="link">A-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/aktiver-ue-20" class="link">Aktive/Ü 20<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/seniorin-ue-35" class="link">Senior/in Ü 35<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings3" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Spieler/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/spieler" class="link">Startseite Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/bis-u-11-spielerin" class="link">Bis U 11-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/u-12-bis-u-15-spielerin" class="link">U 12- bis U 15-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/u-16-bis-u-19-spielerin" class="link">U 16- bis U 19-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/aktive-ue20" class="link">Aktive/r Ü 20<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/seniorin-ue-35" class="link">Senior/in Ü 35<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings4" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Lehrer/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/lehrer" class="link">Startseite Lehrer/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/lehrer/grundschule" class="link">Grundschule<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/lehrer/weiterfuehrende-schule" class="link">Weiterführende Schulen<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings5" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Schiedsrichter/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter" class="link">Startseite Schiedsrichter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/aktiver-schiedsrichterin" class="link">Aktive/r Schiedsrichter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/interessentin" class="link">Interessent/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/funktionaerin" class="link">Funktionär/in<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings6" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Vereinsmitarbeiter/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter" class="link">Startseite Vereinsmitarbeiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/vereinsvorsitzender" class="link">Vereinsvorsitzende/r<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/abteilungsleiterin-fussball" class="link">Abteilungsleiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/jugendleiterin" class="link">Jugendleiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/schatzmeisterin" class="link">Schatzmeister/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/pressesprecherin" class="link">Pressereferent/in<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="tv" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Videos & Foren</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv1">Amateur-TV<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv2">Fotos<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv3">Foren<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv1" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Amateur-TV</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/amateur.tv.magazin" class="link">Magazin<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/amateur.tv.voting/-/rubrik/zdftw" class="link">ZDF Torwandschießen<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/fan.video" class="link">Fanvideos<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv2" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Fotos</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/fan.photo" class="link">Fanfotos<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/fan.photo.alben" class="link">Fotoalben<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv3" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Foren</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/41" class="link">Das neue FUSSBALL.DE<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/11" class="link">Alles zum Amateurfußball<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/21" class="link">Alles, nur kein Amateurfußball<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/31" class="link">Votings und Umfragen<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/91" class="link">Service<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="login" class="flyout-subnav">
			<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Anmelden</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-content"><span></span>Inhalte verwalten<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-account"><span></span>Kontoeinstellungen<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-profile"><span></span>Profil einrichten<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-content" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Inhalte verwalten</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li>
											<a href="https://www.fussball.de/favorites" class="link">Deine Favoriten<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/images.and.videos.overview" class="link">Deine Bilder & Videos<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/account.photoalbum" class="link">Deine Fotoalben<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-mid">
											<a href="https://www.fussball.de/account.admin.widgets" class="link">Deine Widgets<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<div data-user-dependency="{'FBDE_PROFILES':'inarraystartswith'}" data-user="{'FBDE_PROFILES':'TEAM'}">
												<a href="https://www.fussball.de/account.teams" class="link">Deine Mannschaftsseiten<span class="icon-link-arrow"></span></a>
											</div>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/account.news" class="link">Deine Spielberichte & News<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url888927" type="hidden" value="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-account" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Kontoeinstellungen</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li>
											<a href="https://www.fussball.de/account.admin" class="link">Benutzerprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a href="https://www.fussball.de/account.admin.player" class="link">Spielerprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a href="https://www.fussball.de/account.admin.referee" class="link">Schiriprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url888928" type="hidden" value="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-profile" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Profil einrichten</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'notinarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}" class="hidden-small">
											<a href="https://www.fussball.de/register.player?fw_url=http%3A%2F%2Fwww.fussball.de%2Fhomepage" class="link">Spielerprofil einrichten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'notinarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}" class="hidden-small">
											<a href="https://www.fussball.de/register.referee?fw_url=http%3A%2F%2Fwww.fussball.de%2Fhomepage" class="link">Schiriprofil einrichten<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url888929" type="hidden" value="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="search" class="flyout-subnav">
			<div class="container displaystate">
				<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Suche</h4>
				<div class="header-flyout-search">
					<form method="GET" action="//www.fussball.de/suche" data-rest-form>
						<div class="form-group form-dark">
							<div class="search-input">
								<div class="label-wrapper">
									<input data-ng-model="flyoutsearchQuery" name="text" placeholder="Suchbegriff eingeben*" id="flyout-search-query" type="text" value="">
									<label for="flyout-search-query"><span class="icon-search"></span></label>
								</div>
							</div>
							<div data-select-box="single" class="select-wrapper">
								<select size="1" name="restriction">
									<option value="-1">Gesamte Seite</option>
									<option value="CLUB_AND_TEAM">Vereine</option>
									<option value="PLAYER_PROFILE">Spielerprofile</option>
									<option value="FAN_PROFILE">Benutzerprofile</option>
									<option value="REFEREE_PROFILE">Schiedsrichterprofile</option>
									<option value="NEWS">News</option>
									<option value="UGC_NEWS">Mannschafts-News</option>
									<option value="PROFI_NEWS">Profi-Newsflash</option>
								</select>
							</div>
						</div>
						<div class="search-button">
							<button type="submit" class="button button-primary button-block">Finden</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</header><div data-ng-class="{active:flyoutState.isOpen, 'active-layer':layerState.isOpen, 'active-loader':loaderState.isActive}" data-ng-click="closeFlyout()" id="content-block"></div>

		

		<nav class="in-page-share">
	<ul>
		<li class="favorites">
			<ul>
				<li>
					<a href="https://www.fussball.de/add.favorite?fw_url=http%3A%2F%2Fwww.fussball.de%2Fspieltag%2Fbfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden%2F-%2Fstaffel%2F020EQ1DMQ8000003VS54898DVTQF3A0H-G&object-ref=020EQ1DMQ8000003VS54898DVTQF3A0H-G&object-type=competition&text=17%2F18+-+B-Junioren+-+Landesliga+-+Baden%3A+bfv-B-Junioren+Landesliga+Rhein%2FNeckar"><span class="icon-favorits"></span></a>
				</li>
			</ul>
		</li>
		<li class="facebook sharing">
			<a href="" data-share-page="facebook" target="_blank"><span class="icon-facebook"></span></a>
		</li>
		<li class="twitter sharing">
			<a href="" data-share-page="twitter" target="_blank"><span class="icon-twitter"></span></a>
		</li>
		<li class="googleplus sharing">
			<a href="" data-share-page="googleplus" target="_blank"><span class="icon-googleplus"></span></a>
		</li>
	</ul>
</nav>

		<div class="content" data-ng-class="{flyoutopened:flyoutState.isOpen}" >
			


		<section id="stage" class="profile-theme-blue" data-lazyload>
	<div class="fixtures-stage">
		<div class="stage centered grass">
			<div class="container">
				<div class="stage-content">
					<h4>Saison 17/18</h4>
					<h2>bfv-B-Junioren Landesliga Rhein/Neckar</h2>
					<ul class="stage-stats">
						<li><span data-countup="412"></span><span class="text-vert text-vert-goals-total">Tore</span></li>
						<li><span data-countup="5.6"></span><span class="text-vert text-vert-goals-avg">Tore/Spiel</span></li>
					</ul>
					<div class="button-group">
						<a data-scroll-to="table" href="#!/section/table" title="Tabelle" class="button button-primary button-stage">Tabelle</a>
						<a href="http://www.fussball.de/torjaeger/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" title="Top-Torjäger" class="button button-primary button-stage">Top-Torjäger</a>
					</div>
				</div>
			</div>
			<div class="stage-meta">
				<ul class="stage-meta-right">
					<li><span>Staffel-ID: 320115</span><span>Spielklasse: B-Junioren Landesliga</span></li>
					<li class="logo">
						<a href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180">
							<img src="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004180" alt="logo">
						</a>
					</li>
				</ul>
			</div>
			<div class="previous">
				<a rel="prev" href="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-odenwald-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMFC00000CVS54898DVTQF3A0H-G"><span class="icon-angle-light-left"></span><span class="icon-angle-ultralight-left"></span></a>
			</div>
		</div>
	</div>
</section>




<section id="mediastream">
    <div class="wrapper" data-mediastream="http://service.media.fussball.de/api/mediastream/ajax/-/competition/020EQ1DMQ8000003VS54898DVTQF3A0H-G"
         data-mediastream-id="xxxxxx"
         data-streamitemmeta="http://service.media.fussball.de/api/global/ajax_view.html"
         data-offsetleft='{"desktop":0, "tablet":0, "mobile":0}'
         data-user-dependency="{'FBDE_USER_ID':'exist'}"
         data-tv-video-quality-selector-binding="quality" > <!-- [patch:3746] component:quality -->

        <div class="loader" data-ng-class="{loaded:initalized}" data-lazyload></div>

        <div class="stream">
            <div class="info-box counter">
                <span class="primary" data-ng-bind="streamitem.maxIndex">0</span>
                <div class="secondary">Bilder / Videos</div>
            </div>

            <div class="background-wrapper">
                <ul data-itemwidth="180">
                    <li data-ng-repeat="item in streamItems | orderBy:'item.id'" data-mediastreamitem="{{item.id}}" data-ng-class="{active:active, infront:infront, adjusting:adjusting, video:item.type=='video'}">
                        <a data-ng-click="openBigView()">
                            <img data-ng-src="{{item.thumb}}" data-imageload/>
                        </a>
                    </li>

                    <li class="no-uploads" data-mediastreamitemfallback>
                        <span>Zeig&#x27;s uns! Lade dein Video oder Foto hoch!</span>
                    </li>
                </ul>
            </div>

            <div class="info-box upload" data-ng-click="showUpload()">
                <span class="primary">+</span>
                <div class="secondary">Jetzt Hochladen</div>
            </div>
        </div>

        <div class="sub-view" data-ng-class="{show:subView.open, item: subView.current == 'item', upload: subView.current == 'upload'}">
            <div class="sub-view-wrapper">

                <span data-ng-click="closeSubView()" class="icon-close"></span>

                <div class="item-view" data-ng-class="{show:subView.current == 'item'}">
                    <div class="bigimage">
                        <div class="control-wrapper">

                            <p class="itemindex">{{streamitem.content.streamDataIndex+1}} / {{streamitem.maxIndex}}</p>

                            <div class="bigimage-image" data-ng-class="{show:streamitem.content.type == 'image'}">
                                <img data-ng-src="{{streamitem.image}}" alt="galerie" data-imageload='{"setSize":true}'>
                            </div>

                            <div class="bigimage-video" data-ng-class="{show:streamitem.content.type == 'video'}">
								<!-- components::video_player -->
<div class="video-player"  data-video data-swf="//www.fussball.de/static/por/6.80.99.3077/swf/videoplayer.swf">
	<video autobuffer controls data-ng-hide="video.flashFallback()">

	</video>

	<div class="flash-fallback" data-ng-show="video.flashFallback()">

	</div>

	<a href="" class="flashPlayPause" data-ng-show="video.flashFallback()" data-ng-click="playPause()"></a>

</div>
<!-- /components::video_player -->

							</div>

                            <div class="previous" data-ng-class="{available:streamitem.enablePrev}">
								              <a href="javascript://" rel="prev" data-ng-click="prevStreamitem()">
                                	<span class="icon-angle-ultralight-left"></span>
                           		</a>
                            </div>
                            <div class="next" data-ng-class="{available:streamitem.enableNext}">
                            	<a href="javascript://" rel="next" data-ng-click="nextStreamitem()">
                                	<span class="icon-angle-ultralight-right"></span>
                                </a>
                            </div>

                            <!-- snippet::video_quality_horizontal -->
<!-- .hide-qualities - die Klasse wird zur Steuerung der Sichtbarkeit in Media-Stream verwendet! -->
<div class="form-kit" ng-class="{ 'hide-qualities' : !showQualities }" >
  <div class="form-element quality-form-element"
       data-ng-controller="TvVideoQualityController"
       data-radio-group="quality">

      <label class="main quality-level quality-title" >Qualität</label>
      <div class="quality-level quality-entry"
           data-ng-repeat="qualityItem in qualities" >
          <label class="radio small" >
              <span class="radio-button"></span>
              <input type="radio"
                     name="quality"
                     value="{{ qualityItem.value }}" />
              <span class="label">{{ qualityItem.title }}</span>
          </label>
      </div>

  </div>
</div>
<!-- /snippet::video_quality_horizontal -->


                            <div class="mediastream-content">
                                <span class="meta" data-ng-if="streamitem.content.user">
									Hochgeladen am {{streamitem.content.date}} um {{streamitem.content.time}} Uhr von <a data-ng-href="{{streamitem.content.userurl}}">{{streamitem.content.user}}<span class="icon-link-arrow"></span></a>
								</span>
								<span class="meta" data-ng-if="!streamitem.content.user">
									Hochgeladen am {{streamitem.content.date}} um {{streamitem.content.time}} Uhr
								</span>
                                <h3>{{streamitem.content.title}}</h3>
                                <p>
                                    {{streamitem.content.description}}
                                </p>
                                <div class="detailed-informations" data-ng-show="streamitem.content.loaded">
                                    <div class="numberOfViews">
                                        <span data-ng-bind="streamitem.content.views">0</span>
                                        <span class="text" data-ng-pluralize count="streamitem.content.views" when="{'1': 'Aufruf', 'other': 'Aufrufe'}"></span>
                                    </div>
                                    <div class="seperator">|</div>
                                    <div class="number-of-comments">
                                        <span data-ng-bind="streamitem.content.comments">0</span>
                                        <span class="text" data-ng-pluralize count="streamitem.content.comments" when="{'1': 'Kommentar', 'other': 'Kommentare'}"></span>
                                    </div>
                                    <div class="seperator">|</div>
                                    <div class="rating">
                                        <div class="stars">
                                            <span class="star" data-ng-class="{active:getStarRating(1)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(2)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(3)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(4)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(5)}"></span>
                                        </div>
                                        <span data-ng-bind="streamitem.content.ratings">0</span>
                                        <span data-ng-pluralize count="streamitem.content.ratings" when="{'1': 'Bewertung', 'other': 'Bewertungen'}"></span>
                                    </div>
                                </div>
                                <a data-ng-href="{{streamitem.content.targetName}}" class="commentAndShare">Kommentieren, bewerten und melden<span class="icon-link-arrow"></span></a>
                            </div>
                        </div>
                    </div>
				</div>
                <div class="upload-view upload-component" data-ng-class="{show:subView.current == 'upload'}" data-fileupload="http://service.media.fussball.de/api/upload/ajax"  data-fileupload-check="true" data-postdef='{"key1":"value1", "key2":"value2", "key3":"value3"}'>
                        <!-- components::upload -->
<form id="fileupload" action="#" method="POST" enctype="multipart/form-data">
    <div class="header-intro">
        <div class="before-upload">
            <h3 class="headline">
                Zeig’s uns! Lade deine Bilder und Videos hoch!
            </h3>

            <p class="upload-informations">
                Mögliche Bildformate sind JPG, PNG und GIF. Die Dateigröße sollte 2 MB nicht überschreiten. Wir unterstützen folgende Videoformate MPG, MP4, AVI, MOV und WMV. Dein Video sollte nicht größer als 100 MB sein.
				<br>
				Bitte beachte nach dem Veröffentlichen Deiner Bilder und Videos, dass die Konvertierung der Dateien etwas Zeit beansprucht, sodass Du die Bilder bzw. Videos nicht sofort siehst. Habe bitte etwas Geduld.
            </p>

            <div class="form-kit">
                <div class="form-element buttons step">
                    <span class="button button-primary add-files" data-ng-class="{disabled: disabled}">
                        <span class="text"><span>+</span>Dateien hinzufügen</span>
                        <input data-ng-file-select type="file" multiple>
                    </span>
                    <button class="button button-primary" type="button" data-ng-click="uploader.uploadAll()" data-ng-disabled="!uploader.getNotUploadedItems().length">
                        Upload starten
                    </button>
                    <button class="button button-primary" type="button" data-ng-click="releaseAllFiles(uploader.queue)" data-ng-show="allFilesUploaded(uploader.queue)" data-ng-disabled="!allFilesReadyTorelease(uploader.queue)">
                        Alle Veroeffentlichen
                    </button>
                </div>
            </div>
        </div>
    </div>
</form>

<div class="files">
    <ul>
        <li data-ng-repeat="item in uploader.queue" data-meta data-url-release="https://service.media.fussball.de/api/upload/release/-/competition/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-url-update="https://service.media.fussball.de/api/upload/update/-/competition/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-url-delete="https://service.media.fussball.de/api/upload/delete">

            <div class="item-wrapper">
                <div class="file-thumbnail-wrapper">
                    <div class="file-thumbnail">
                        <div data-ng-show="uploader.isHTML5 && controller.filetype(item.file) == 'image'" data-thumb="{ file: item.file, height: 70 }"></div>
                        <img data-ng-show="!uploader.isHTML5 && controller.filetype(item.file) == 'image'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_image.png" alt="">
                        <img data-ng-show="controller.filetype(item.file) == 'video'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_video.png" alt="">
                        <img data-ng-show="controller.filetype(item.file) == 'default'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_default.png" alt="">
                    </div>
                </div>

                <div class="file-meta" data-ng-class="{'video':item.isUploaded && item.isSuccess && controller.filetype(item.file) == 'video'}">
                    <span class="file-name">
                        {{item.file.name}}
                    </span>
                    <span class="file-size" data-ng-show="uploader.isHTML5">
                        {{ item.file.size/1024/1024|number:2 }} Mb
                    </span>
                    <span class="file-error" data-ng-show="item.error.show">
                        {{item.error.plainText ? item.error.message : (item.error.message | translate)}}
                    </span>
                    <div class="span file-convert" data-ng-show="item.isUploaded && item.isSuccess && controller.filetype(item.file) == 'video'">
                        Dein hochgeladenes Video wird noch konvertiert, was einige Zeit dauern kann. Du kannst dein Video später unter &quot;Meine Bilder und Videos&quot; freigeben und eine Beschreibung hinzufügen.
                    </div>
                </div>

                <div class="file-progress" data-ng-show="item.isUploading && uploader.isHTML5">
                    <div class="file-progressbar" data-ng-style="{ 'width': item.progress + '%' }"></div>
                </div>

                <div class="file-action">
                    <div class="form-kit">
                        <div class="form-element buttons step">
                            <button class="button file-button-cancel" type="button" data-ng-click="item.cancel()" data-ng-show="item.isUploading">
                                <span class="icon-close"></span>
                                Abbrechen
                            </button>
                            <button class="button file-button-delete" type="button" data-ng-click="item.remove()" data-ng-show="!item.isUploading && !item.isSuccess">

                                Löschen
                            </button>
                            <button class="button file-button-edit" type="button" data-ng-click="item.tab = !item.tab"  data-ng-show="item.isUploaded && item.isSuccess">
                                <span class="icon-edit"></span>
                                Bearbeiten
                            </button>
                            <button class="button button-primary file-button-release" data-ng-click="releaseItem(item)" type="button" data-ng-show="item.isUploaded && item.isSuccess" data-ng-disabled="!checkMetaTitle()">
                                Veröffentlichen
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="tab" data-ng-show="item.tab">
                <form ng-submit>
                    <div class="form-element text">
                        <label class="main">Titel
                            <input type="text" data-ng-model="metaTitle" name="title" maxlength="100">
                            <p data-remainingchars="nomodel" data-ng-cloak class="ng-cloak">{{remainingchars}} Zeichen möglich</p>
                        </label>
                    </div>

                    <div class="form-element textarea">
                        <label class="main">Beschreibung
                            <textarea name="message" data-ng-model="metaMessage" maxlength="1000" cols="30" rows="10"></textarea>
                            <p data-remainingchars="nomodel" data-ng-cloak class="ng-cloak">{{remainingchars}} Zeichen möglich</p>
                        </label>
                    </div>

                    <div class="form-element buttons step">
                        <a href="javascript://" data-ng-click="abortEdit()">Abbrechen<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="updateItem(item)">Speichern<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="deleteItem(item)">Löschen<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="overwriteSiblings(item)">Titel/Text für alle Dateien übernehmen<span class="icon-link-arrow"></span></a>
                    </div>
                </form>
            </div>

        </li>
    </ul>
</div>
<!-- /components::upload -->

                </div>
            </div>
        </div>
    </div>
</section>


<section class="wm-section">
	<div data-wm-type="super" class="wm-container">
		<div class="wm-container-inner">
			<div data-ad-sizes="[[320,50], [468,60], [728,90]]" data-ad-local-link="http://www.fussball.de/newsdetail/push-ticker-und-mehr-das-bietet-unsere-app/-/article-id/127931#!/section/stage" data-ad-breakpoints="phone,tablet,desktop" data-ad-local-image="{'desktop': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-sb.png', 'tablet': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-fsb.png', 'phone':'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-mb.png'}" class="wm-iframe" data-ad-local-link-target="_top">
				<p>Anzeige</p>
				<div id="slot-3688414">
					<script type="text/javascript">wmConfig.registerRenderSlot('slot-3688414');</script>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="matches">
	<div data-active-class="active" data-type="link" class="tab-group" data-tab-group>
		<a class="prev"><span class="icon-angle-left"></span></a>
		<ul>
			<li class="active">
				<a href="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G#!/section/matches">Aktuell</a>
			</li>
			<li>
				<a href="http://www.fussball.de/spieltag/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G#!/section/matches">Spieltage / Tabellen</a>
			</li>
			<li>
				<a href="http://www.fussball.de/spielplan/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G#!/section/matchplan">Staffelspielplan</a>
			</li>
			<li>
				<a href="http://www.fussball.de/torjaeger/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G#!/section/top-scorer">Torjäger</a>
			</li>
		</ul>
		<a class="next"><span class="icon-angle-right"></span></a>
	</div>
	<div class="fixtures-matches-table">
		<div class="table-container">
			<table class="table table-striped table-full-width thead">
				<thead>
					<tr class="thead hidden-small">
						<th class="align-right"><span class="hidden-small inline">Datum |&nbsp;</span>Zeit</th>
						<th colspan="2">Heim</th>
						<th>Gast</th>
						<th><span class="hidden-small">Ergebnis</span><span class="visible-small">Erg.</span></th>
						<th><span class="visible-full">Info</span></th>
						<th></th>
						<th></th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					<tr class="row-headline visible-small">
						<td colspan="9"><span data-obfuscation="xc2jj6ju">&#xE6EC;&#xE71D;&#xE6D6;&#xE6B1;&#xE6D3;&#xE67F;&#xE6C9;&#xE6E3;&#x0020;&#xE730;&#xE775;&#xE712;&#xE6BC;&#xE710;&#xE70B;&#xE704;&#xE75F;&#xE723;&#xE772;</span></td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span data-obfuscation="xc2jj6ju" class="hidden-small inline">&#xE74E;&#xE770;&#xE744;&#x0020;&#xE743;&#xE6F5;&#xE768;&#xE6A9;&#xE663;&#xE6AC;&#xE696;&#xE757;&#x0020;&#x007c;&nbsp;</span><span data-obfuscation="xc2jj6ju">&#xE743;&#xE6E7;&#xE777;&#xE6A9;&#xE75F;</span></td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/tsg-91-09-luetzelsachsen-tsg-91-09-luetzelsachsen-baden/-/saison/1718/team-id/011MIC2U1G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="TSG 91/09 Lützelsachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800009QVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									TSG 91/&#8203;09 Lützelsachsen
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/tsg-91-09-luetzelsachsen-fc-astoria-walldorf-2/-/spiel/020GBC1TNC000000VS54898EVVII0TR2"><span data-obfuscation="osonfujd" class="score-left">&#xE6A6;</span><span class="colon">:</span><span data-obfuscation="osonfujd" class="score-right">&#xE657;</span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/tsg-91-09-luetzelsachsen-fc-astoria-walldorf-2/-/spiel/020GBC1TNC000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr>
						<td class="column-date"><span data-obfuscation="xc2jj6ju">&#xE71A;&#xE6EE;&#xE66D;&#xE720;&#xE6CE;</span></td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sv-98-schwetzingen-sv-98-schwetzingen-baden/-/saison/1718/team-id/011MIF5TEC000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SV 98 Schwetzingen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A4VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									SV 98 Schwetzingen
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/sg-dossenheim-ziegelh-peterstal-1-fc-sportfr-dossenheim-baden/-/saison/1718/team-id/011MIC855G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Dossenheim/Ziegelhausen-Peterstal" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006NVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									SG Dossenheim/&#8203;Ziegelhausen-Peterstal
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/sg-dossenheim-ziegelh-peterstal-1-sv-98-schwetzingen/-/spiel/020GBC1U20000000VS54898EVVII0TR2"><span data-obfuscation="osonfujd" class="score-left">&#xE694;</span><span class="colon">:</span><span data-obfuscation="osonfujd" class="score-right">&#xE659;</span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/sg-dossenheim-ziegelh-peterstal-1-sv-98-schwetzingen/-/spiel/020GBC1U20000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span data-obfuscation="xc2jj6ju">&#xE723;&#xE6B8;&#xE661;&#xE6E7;&#xE728;</span></td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-waibstadt-meckesheim-moenchzell-daisbach-sg-waibstadt-baden/-/saison/1718/team-id/01SMKMQ6C8000000VS548985VU8O1RK1" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Waibstadt/Meckesheim-Mönchzell/Daisbach" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800005SVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									SG Waibstadt/&#8203;Meckesheim-Mönchzell/&#8203;Daisbach
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/vfl-kurpfalz-mannheim-neckarau-vfl-kurpfalz-mannheim-neckarau-baden/-/saison/1718/team-id/01E03IV450000000VV0AG811VTA8FO8N" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="VfL Kurpfalz Mannheim-Neckarau" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008RVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									VfL Kurpfalz Mannheim-Neckarau
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/vfl-kurpfalz-mannheim-neckarau-sg-waibstadt-meckesheim-moenchzell-daisbach/-/spiel/020GBC1UOG000000VS54898EVVII0TR2"><span data-obfuscation="osonfujd" class="score-left">&#xE6A9;</span><span class="colon">:</span><span data-obfuscation="osonfujd" class="score-right">&#xE680;</span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/vfl-kurpfalz-mannheim-neckarau-sg-waibstadt-meckesheim-moenchzell-daisbach/-/spiel/020GBC1UOG000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr>
						<td class="column-date"><span data-obfuscation="xc2jj6ju">&#xE656;&#xE728;&#xE661;&#xE726;&#xE738;</span></td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-zuzenhausen-fc-zuzenhausen-baden/-/saison/1718/team-id/01E0PF8DBG000000VV0AG80NVV2L7DJE" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Zuzenhausen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000060VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									FC Zuzenhausen
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/tsg-62-09-weinheim-tsg-62-09-weinheim-baden/-/saison/1718/team-id/011MICLQ1K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="TSG 62/09 Weinheim" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A8VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									TSG 62/&#8203;09 Weinheim
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/tsg-62-09-weinheim-fc-zuzenhausen/-/spiel/020GBC1V3O000000VS54898EVVII0TR2"><span data-obfuscation="osonfujd" class="score-left">&#xE68D;</span><span class="colon">:</span><span data-obfuscation="osonfujd" class="score-right">&#xE6A9;</span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/tsg-62-09-weinheim-fc-zuzenhausen/-/spiel/020GBC1V3O000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span data-obfuscation="xc2jj6ju"></span></td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-eppingen-2-vfb-eppingen-baden/-/saison/1718/team-id/01A4655LQ4000000VV0AG811VSUI9EOJ" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="VfB Eppingen 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800004VVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180"></span></div>
								<div class="club-name">
									VfB Eppingen 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border"><span class="info-text">spielfrei</span></td>
						<td class="column-score"></td>
						<td class="column-detail"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
				</tbody>
			</table>
		</div>
		<div data-toggle=".legend > span, .note > span" class="table-meta">
			<ul class="functions">
				<li class="legend"><span data-toggle-content=".table-legend">Legende<span class="icon-angle-down"></span></span></li>
				<li class="print">
					<a href="http://www.fussball.de/spieltagsuebersicht.druck/-/max/999/mode/PRINT/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" target="_blank">Drucken<span class="icon-link-arrow"></span></a>
				</li>
			</ul>
			<div class="table-legend">
				<h3>Kürzel bei einem Spiel</h3>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>u</span></div>
							<div class="description">(U) Sportgerichtsurteil (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Annuliert</span></div>
							<div class="description">Annullierung</div>
						</div>
						<div class="column">
							<div class="item"><span>v</span></div>
							<div class="description">(V) Verwaltungsentscheid (bestätigt)</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>Absetzung</span></div>
							<div class="description">Spielabsetzung</div>
						</div>
						<div class="column">
							<div class="item"><span>w</span></div>
							<div class="description">(W) Wertung Spielinstanz (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Ausfall</span></div>
							<div class="description">Spielausfall</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>t</span></div>
							<div class="description">(T) Testspiel (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Abbruch</span></div>
							<div class="description">Spielabbruch</div>
						</div>
						<div class="column">
							<div class="item"><span>zg.</span></div>
							<div class="description">Diese Mannschaft wurde zurückgezogen, die Ergebnisse werden aber eingerechnet.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>Nichtantritt BEIDE</span></div>
							<div class="description">nicht angetretene Mannschaften</div>
						</div>
						<div class="column">
							<div class="item"><span>Nichtantritt HEIM</span></div>
							<div class="description">nicht angetreten HEIM-Mannschaft</div>
						</div>
						<div class="column">
							<div class="item"><span>Nichtantritt GAST</span></div>
							<div class="description">nicht angetreten GAST-Mannschaft</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>nV</span></div>
							<div class="description">nach Verlängerung</div>
						</div>
						<div class="column">
							<div class="item"><span>nE</span></div>
							<div class="description">nach Elfmeterschießen</div>
						</div>
					</div>
				</div>
				<h3>Sonstiges</h3>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>**</span></div>
							<div class="description">Die Anstoßzeit steht noch nicht fest oder ist nicht bekannt.</div>
						</div>
						<div class="column">
							<div class="item"><span>o.E.</span></div>
							<div class="description">Keine Ergebnisanzeige, da die Staffel nicht im Leistungsbetrieb spielt.</div>
						</div>
						<div class="column">
							<div class="item"><span>oW</span></div>
							<div class="description">Mannschaften mit diesem Kennzeichen spielen außer Konkurrenz.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span class="icon-verified"></span></div>
							<div class="description">Ergebnis bestätigt</div>
						</div>
						<div class="column">
							<div class="item"><span>Live</span></div>
							<div class="description">Liveticker</div>
						</div>
						<div class="column">
							<div class="item"><span>SPIELFREI</span></div>
							<div class="description">An diesem Datum hat die Mannschaft spielfrei.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span class="icon-article"></span></div>
							<div class="description">Spielbericht vorhanden</div>
						</div>
						<div class="column">
							<div class="item"><span class="icon-foto"></span></div>
							<div class="description">Foto oder Video vorhanden</div>
						</div>
						<div class="column">
							<div class="item"><span class="icon-video"></span></div>
							<div class="description">Livestream oder Highlights vorhanden</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="table">
	<div data-ng-controller="AjaxController" id="tables-and-presenter-container">
		<div class="presenter post">
			<h6>Die Tabelle präsentiert von:</h6>
			<a href="http://www.fussball.de/partner">
				<img src="http://www.fussball.de/static/por/6.80.99.3077/images/partner/presenter_post_logo.png" alt="presenter">
			</a>
		</div>
		<div data-toggle="li a" data-type="ajax" class="tab-group has-icons" data-tab-group>
			<ul>
				<li class="on">
					<a data-tracking-name="wettbewerb_tabelle/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_tabelle" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-table"></span>Tabelle</a>
				</li>
				<li>
					<a data-tracking-name="wettbewerb_hinrueck/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_hinrueck" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table.rounds/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table.rounds/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table.rounds/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-rounds"></span>Hin-/ Rückrunde</a>
				</li>
				<li>
					<a data-tracking-name="wettbewerb_heimauswaerts/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_heimauswaerts" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table.home.away/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table.home.away/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table.home.away/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-home-away"></span>Heim/ Auswärts</a>
				</li>
				<li>
					<a data-tracking-name="wettbewerb_fieberkurve/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_fieberkurve" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table.fevercurve/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table.fevercurve/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table.fevercurve/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-curve"></span>Fieberkurve</a>
				</li>
				<li>
					<a data-tracking-name="wettbewerb_kreuztabelle/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_kreuztabelle" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table.cross/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table.cross/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table.cross/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-cross-table"></span>Kreuztabelle</a>
				</li>
				<li>
					<a data-tracking-name="wettbewerb_fairness/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-pagename-short="wettbewerb" data-tracking-channel="ligen" data-ajax-type="html" data-tracking-pagename-long="wettbewerb_fairness" data-ajax-target="#tables-and-presenter-container" data-tracking-subchannel="aktuell" data-ajax-resource="http://www.fussball.de/ajax.actual.table.fairness/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" href="http://www.fussball.de/ajax.actual.table.fairness/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.actual.table.fairness/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}" data-ajax><span class="icon-fairness"></span>Fairness</a>
				</li>
			</ul>
		</div>
		<div id="fixture-league-tables" class="table-container fixtures-league-table">
			<table class="table table-striped table-full-width">
				<thead>
					<tr class="thead">
						<th colspan="2"><span class="visible-small">Pl.</span><span class="hidden-small">Platz</span></th>
						<th class="column-large">Mannschaft</th>
						<th><span class="visible-small">Sp.</span><span class="hidden-small">Spiele</span></th>
						<th class="hidden-small">G</th>
						<th class="hidden-small">U</th>
						<th class="hidden-small">V</th>
						<th><span class="visible-small">Torv.</span><span class="hidden-small">Torverhältnis</span></th>
						<th class="hidden-small">Tordifferenz</th>
						<th><span class="visible-small">Pkt.</span><span class="hidden-small">Punkte</span></th>
					</tr>
				</thead>
				<tbody>
					<tr class="row-promotion">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							1.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="FC Astoria Walldorf 2">
								</div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">14</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">0</td>
						<td class="no-wrap">105 : 9</td>
						<td class="hidden-small">96</td>
						<td class="column-points">42</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							2.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfl-kurpfalz-mannheim-neckarau-vfl-kurpfalz-mannheim-neckarau-baden/-/saison/1718/team-id/01E03IV450000000VV0AG811VTA8FO8N" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008RVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfL Kurpfalz Mannheim-Neckarau">
								</div>
								<div class="club-name">
									VfL Kurpfalz Mannheim-Neckarau
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">9</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">3</td>
						<td class="no-wrap">42 : 22</td>
						<td class="hidden-small">20</td>
						<td class="column-points">28</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							3.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/tsg-62-09-weinheim-tsg-62-09-weinheim-baden/-/saison/1718/team-id/011MICLQ1K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A8VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="TSG 62/09 Weinheim">
								</div>
								<div class="club-name">
									TSG 62/&#8203;09 Weinheim
								</div>
							</a>
						</td>
						<td>12</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">4</td>
						<td class="no-wrap">35 : 20</td>
						<td class="hidden-small">15</td>
						<td class="column-points">22</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							4.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-gartenstadt-vfb-gartenstadt-baden/-/saison/1718/team-id/011MIFD46K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008NVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfB Gartenstadt">
								</div>
								<div class="club-name">
									VfB Gartenstadt
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">6</td>
						<td class="no-wrap">42 : 50</td>
						<td class="hidden-small">-8</td>
						<td class="column-points">22</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-up-right"></span></td>
						<td class="column-rank">
							5.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-baiertal-schatthausen-spvgg-baiertal-baden/-/saison/1718/team-id/011MIB1C40000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006IVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Baiertal/Schatthausen">
								</div>
								<div class="club-name">
									SG Baiertal/&#8203;Schatthausen
								</div>
							</a>
						</td>
						<td>15</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">42 : 56</td>
						<td class="hidden-small">-14</td>
						<td class="column-points">21</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							6.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sv-98-schwetzingen-sv-98-schwetzingen-baden/-/saison/1718/team-id/011MIF5TEC000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A4VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SV 98 Schwetzingen">
								</div>
								<div class="club-name">
									SV 98 Schwetzingen
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">20 : 32</td>
						<td class="hidden-small">-12</td>
						<td class="column-points">16</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-up-right"></span></td>
						<td class="column-rank">
							7.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-waibstadt-meckesheim-moenchzell-daisbach-sg-waibstadt-baden/-/saison/1718/team-id/01SMKMQ6C8000000VS548985VU8O1RK1" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800005SVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Waibstadt/Meckesheim-Mönchzell/Daisbach">
								</div>
								<div class="club-name">
									SG Waibstadt/&#8203;Meckesheim-Mönchzell/&#8203;Daisbach
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">33 : 46</td>
						<td class="hidden-small">-13</td>
						<td class="column-points">16</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							8.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/tsg-91-09-luetzelsachsen-tsg-91-09-luetzelsachsen-baden/-/saison/1718/team-id/011MIC2U1G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800009QVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="TSG 91/09 Lützelsachsen">
								</div>
								<div class="club-name">
									TSG 91/&#8203;09 Lützelsachsen
								</div>
							</a>
						</td>
						<td>12</td>
						<td class="hidden-small">4</td>
						<td class="hidden-small">3</td>
						<td class="hidden-small">5</td>
						<td class="no-wrap">24 : 25</td>
						<td class="hidden-small">-1</td>
						<td class="column-points">15</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							9.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-dossenheim-ziegelh-peterstal-1-fc-sportfr-dossenheim-baden/-/saison/1718/team-id/011MIC855G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006NVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Dossenheim/Ziegelhausen-Peterstal">
								</div>
								<div class="club-name">
									SG Dossenheim/&#8203;Ziegelhausen-Peterstal
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">9</td>
						<td class="no-wrap">21 : 58</td>
						<td class="hidden-small">-37</td>
						<td class="column-points">15</td>
					</tr>
					<tr class="row-relegation odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							10.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-eppingen-2-vfb-eppingen-baden/-/saison/1718/team-id/01A4655LQ4000000VV0AG811VSUI9EOJ" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800004VVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfB Eppingen 2">
								</div>
								<div class="club-name">
									VfB Eppingen 2
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">4</td>
						<td class="hidden-small">2</td>
						<td class="hidden-small">7</td>
						<td class="no-wrap">37 : 33</td>
						<td class="hidden-small">4</td>
						<td class="column-points">14</td>
					</tr>
					<tr class="row-relegation">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							11.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-zuzenhausen-fc-zuzenhausen-baden/-/saison/1718/team-id/01E0PF8DBG000000VV0AG80NVV2L7DJE" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000060VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="FC Zuzenhausen">
								</div>
								<div class="club-name">
									FC Zuzenhausen
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">2</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">11</td>
						<td class="no-wrap">11 : 61</td>
						<td class="hidden-small">-50</td>
						<td class="column-points">6</td>
					</tr>
				</tbody>
			</table>
			<div data-toggle=".legend > span, .note > span" class="table-meta">
				<ul class="functions">
					<li class="legend"><span data-toggle-content=".table-legend">Legende<span class="icon-angle-down"></span></span></li>
					<li class="note"><span data-toggle-content=".tab-note">Hinweis zur Tabelle<span class="icon-angle-down"></span></span></li>
					<li class="print">
						<a href="http://www.fussball.de/spieltagsuebersicht.druck/-/max/999/mode/PRINT/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" target="_blank">Drucken<span class="icon-link-arrow"></span></a>
					</li>
				</ul>
				<div class="table-legend">
					<h3>Bereich "Kürzel bei der Mannschaft"</h3>
					<div class="row">
						<div class="wrapper">
							<div class="column">
								<div class="item"><span>oW</span></div>
								<div class="description">Diese Mannschaft spielt in dieser Staffel nicht mehr mit, die Ergebnisse werden aber eingerechnet</div>
							</div>
							<div class="column">
								<div class="item"><span>zg.</span></div>
								<div class="description">Diese Mannschaft wurde zurückgezogen, die Ergebnisse werden aber eingerechnet</div>
							</div>
							<div class="column">
								<div class="item"><span>SW</span></div>
								<div class="description">Für diese Mannschaft ist eine separate Sonderwertung eingerechnet</div>
							</div>
						</div>
					</div>
					<h3>Bereich Trend</h3>
					<div class="row">
						<div class="wrapper">
							<div class="column">
								<div class="item"><span class="icon-arrow-up-right"></span></div>
								<div class="description">Tabellenplatz hat sich im Vergleich zum vorherigen Spieltag verbessert</div>
							</div>
							<div class="column">
								<div class="item"><span class="icon-arrow-right"></span></div>
								<div class="description">Tabellenplatz bleibt im Vergleich zum vorherigen Spieltag unverändert</div>
							</div>
							<div class="column">
								<div class="item"><span class="icon-arrow-down-right"></span></div>
								<div class="description">Tabellenplatz hat sich im Vergleich zum vorherigen Spieltag verschlechtert</div>
							</div>
						</div>
					</div>
				</div>
				<div class="tab-note">
					<h3>Hinweis zur Tabellenrechnung</h3>
					<p>Der SKV Sandhofen hat seine Mannschaft vom Spielbetrieb zurück gezogen und steht somit als erster Absteiger fest !!  17.10.17 S.B.</p>
				</div>
			</div>
		</div>
	</div>
	<div data-toggle=".tab" class="fixtures-teaser-contact-widget teaser-group double" data-toggle-close=".link-close">
		<div class="container">
			<div class="column-one">
				<div class="tab">
					<h3 data-on-click="{'type': 'triggerClick', 'selector': '.captcha > a', 'return': 'false'}"><span class="icon-contact"></span>Falsches Ergebnis melden</h3>
				</div>
				<div class="tab-content">
					<a href="#" class="link-close"><span class="icon-close"></span></a>
					<div class="inner">
						<form data-ajax-type="html" data-ng-controller="AjaxController" data-ajax-target=".contact-form-wrapper" data-ajax-resource="http://www.fussball.de/ajax.contact.form/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" class="contact-form-wrapper" data-ajax="replace" data-ajax-method="post" data-tracking="{'href':'http://www.fussball.de/ajax.contact.form/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G'}">
							<div class="container">
								<p class="description">Trotz aller Sorgfalt können hin und wieder Fehler auftreten. Solltest Du also z.B. auf falsche Ergebnisse oder Tabellenstände stoßen – Kein Problem. Gib dem zuständigen Staffelleiter einfach einen Hinweis. Vielen Dank!</p>
							</div>
							<div class="container contact-form form-small">
								<div class="column-left">
									<input data-ng-model="ngFirstname" name="firstname" placeholder="Dein Vorname*" type="text" value="" class="input-firstname" data-ajaxmodel="firstname">
									<input data-ng-model="ngLastname" name="lastname" placeholder="Dein Nachname*" type="text" value="" class="input-lastname" data-ajaxmodel="lastname">
									<input data-ng-model="ngSender" name="address" placeholder="Deine E-Mail-Adresse*" type="text" value="" class="input-email" data-ajaxmodel="address">
									<input data-ng-model="ngSubject" data-ng-init="ngSubject='Falsches Ergebnis im Wettbewerb bfv-B-Junioren Landesliga Rhein/Neckar'" name="subject" placeholder="Dein Betreff*" type="text" value="Falsches Ergebnis im Wettbewerb bfv-B-Junioren Landesliga Rhein/Neckar" class="input-subject" data-ajaxmodel="subject">
									<textarea data-ng-model="content" name="content" placeholder="Deine Nachricht*" data-ajaxmodel="content"></textarea>
								</div>
								<div class="column-right">
									<div id="captcha_1" class="captcha">
										<div>
											<img alt="renew captcha">
										</div>
										<a data-ajax-type="html" data-ajax-target=".contact-form-wrapper #captcha_1" data-ajax-resource="//www.fussball.de/ajax.captcha/-/captcha-scope/.contact-form-wrapper" href="//www.fussball.de/ajax.captcha/-/captcha-scope/.contact-form-wrapper" data-ajax-method="post" data-tracking="{'href':'//www.fussball.de/ajax.captcha/-/captcha-scope/.contact-form-wrapper'}" data-ajax><span class="icon-reload"></span></a>
										<input data-ng-model="digest" name="captcha-digest" type="hidden" value="" data-ajaxmodel="captcha-digest">
									</div>
									<input data-ng-model="securityCode" name="captcha-code" placeholder="Sicherheitscode*" type="text" value="" data-ajaxmodel="captcha-code">
									<button class="button button-primary">Nachricht senden</button>
									<p class="info">* Pflichtfelder</p>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
			<div class="column-two">
				<div data-user-dependency="{'FBDE_USER_ID':'exist'}" class="tab" data-toggle-name="widget">
					<h3><span class="icon-widget"></span>Widget generieren</h3>
				</div>
				<div class="tab-content widget-tab-container">
					<a href="#" class="link-close"><span class="icon-close"></span></a>
					<div class="inner">
						<div class="widget-wrapper">
							<div class="container">
								<h4 class="description">Hier kannst Du diese Tabelle als Widget für Deine Homepage generieren.</h4>
								<a href="https://www.fussball.de/account.admin.widgets?action=CREATE&object-ref=020EQ1DMQ8000003VS54898DVTQF3A0H-G&type=1" class="button button-primary">Widget erzeugen</a>
								<p class="footnote">Fussball.de Widget: Wettbewerb 020EQ1DMQ8000003VS54898DVTQF3A0H-G</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<section id="news">
	<div class="news-list-related news-list">
		<div class="container grid-view">
			<ul>
				<li class="item nth1"><article class="news-article" >
                    <a href="/newsdetail/90-2-torwart-dahmen-trifft-zum-ausgleich/-/article-id/184919">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_027f0868f8.jpg',
        																		'medium': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_3da102e27d.jpg',
        																		'large': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_4cbab2a1af.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Regionalliga Südwest


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 17:20
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>90.+2: Torwart Dahmen trifft zum Ausgleich!</span>
        												</h2>
                            </div>
                            <p class="excerpt">Ein furioses Ende gab es beim 1:1 zwischen der zweiten Mannschaft des FSV Mainz 05 und der U 23 des VfB Stuttgart in einer Partie vom 27. Spieltag in der Regionalliga Südwest. Den Ausgleichstreffer markierte FSV-Torhüter Finn Dahmen (90.+2) nach einem Eckball aus dem Gewühl heraus. Zuvor hatte Jan Ferdinand die Stuttgarter früh in Führung gebracht.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth2"><article class="news-article" >
                    <a href="/newsdetail/finaltag-der-amateure-22-klubs-schon-dabei/-/article-id/183677">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_2374543e9c.jpg',
        																		'medium': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_81e2a69843.jpg',
        																		'large': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_55d9267f9b.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                                    
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Magazin


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 13:40
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>Finaltag der Amateure: 22 Klubs schon dabei</span>
        												</h2>
                            </div>
                            <p class="excerpt">Alle Landespokalendspiele an einem Tag. Alle Landespokalendspiele live im Fernsehen. In einer siebenstündigen Konferenzschaltung, von der ARD bundesweit übertragen. Am 21. Mai geht der <i>Finaltag der Amateure</i> in seine dritte Runde. 22 Teilnehmer stehen bereits fest. <strong>FUSSBALL.DE</strong> gibt den Überblick.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth3"><article class="news-article" >
                    <a href="/newsdetail/traum-dfb-pokal-landespokale-im-ueberblick/-/article-id/172840">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201708/csm_148053-123_3ae87edf42.jpg',
        																		'medium': 'fileadmin/_processed_/201708/csm_148053-123_57b36a8d48.jpg',
        																		'large': 'fileadmin/_dfbdam/148053-123.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Service


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 07:00
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>Traum DFB-Pokal: Landespokale im Überblick</span>
        												</h2>
                            </div>
                            <p class="excerpt">Über die Landespokale haben auch die Amateurvereine in ganz Deutschland die Chance auf den <i>Finaltag der Amateure</i> und die große Bühne im DFB-Pokal. Sieben Endspielpaarungen stehen bereits fest. <strong>FUSSBALL.DE</strong> gibt den aktuellen Überblick über alle Landespokalwettbewerbe.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth4">
					<div class="news-teaser-two-rows">
						<a style="background-image: url(http://www.fussball.de/static/cms/6.80.99.3077/images/news/activitystream/teaser_association_bg1_300x300.jpg);" href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180">
							<div class="teaser-row">
								<div class="teaser-cell">
									<div class="category"><span>Landesverband</span></div>
									<span class="icon-hexagon"><img src="//www.fussball.de/export.media/-/action/getLogo/format/9/id/0123456789ABCDEF0123456700004180" alt="Baden"></span>
								</div>
							</div>
							<div class="teaser-row">
								<div class="teaser-cell">
									<p class="large">Badischer Fußball-Verband</p>
									<p class="link">Zum Verband</p>
								</div>
							</div>
						</a>
					</div>
				</li>
				<li class="item nth5"><div class="news-teaser-default" style="background-image: url(/assets/-/id/aufstellungsgrafik-409x430.jpg);">
	<a href="http://www.fussball.de/newsdetail/der-grosse-ueberblick-alles-zu-fussballde/-/article-id/116306">
		<div class="inner">
			<p class="large">
				Spitzenspiel.
				<br>
				Spitzen-Look.
			</p>
			<p class="link">Alles rund um FUSSBALL.DE</p>
		</div>
	</a>
</div></li>
				<li class="item nth6"><div class="news-teaser-default" style="background-image: url(/assets/-/id/Torwand-409x430.jpg);">
	<a href="/amateur.tv.voting/-/rubrik/zdftw" target="_blank">
		<div class="category"><span>Service</span></div>
		<div class="inner">
			<p class="large">
				Drei unten.
				<br>
				Drei Oben.
			</p>
			<p class="link">Wir bringen Dich an die ZDF-Torwand</p>
		</div>
	</a>
</div></li>
			</ul>
		</div>
	</div>
</section>

			<section>
	<div class="cookie-advise">
		<div class="container">
			<div class="cookie-advise-content">
				<h3>Cookie Richtlinie</h3>
				<p>Um FUSSBALL.DE benutzerfreundlich zu gestalten, setzen wir Cookies ein. Cookies sind kleine Dateien, die vom Browser verwaltet und für einen späteren Abruf bereitgehalten werden, um die Nutzung von FUSSBALL.DE zu ermöglichen oder zu erleichtern. Sie dienen auch dazu um notwendige Statistiken zu erstellen. Teilweise werden auch Cookies von Dritten (z.B. Google und Facebook) eingesetzt. Mit der weiteren Nutzung unserer Dienste erklärst du dich damit einverstanden, dass wir Cookies verwenden. Du kannst die Cookie-Einstellung auch selbst verändern.  <span class="cookie-advise-content-link-container"><a href="http://www.fussball.de/privacy" class="cookie-advise-content-link">Mehr über unsere Cookies kannst du hier erfahren</a><span class="icon-link-arrow"></span></span></p>
			</div>
			<div class="cookie-advise-links">
				<a href="http://www.fussball.de/cookie.settings" class="cookie-advise-link cookie-advise-settings">Cookie-Einstellungen<span class="icon-link-arrow"></span></a>
				<span data-ng-click="setAllCookies()" class="cookie-advise-link cookie-advise-accept" data-cookie-setting>Cookies akzeptieren</span>
			</div>
		</div>
	</div>
</section>
		</div>
		<footer>
	<div id="sharing" class="visible-small">
		<h6>Teile diese Seite</h6>
		<ul>
			<li class="whatsapp mobile-only">
				<a href="" data-share-page="whatsapp" target="_blank"><span class="icon-whatsapp"></span></a>
			</li>
			<li class="facebook">
				<a href="" data-share-page="facebook" target="_blank"><span class="icon-facebook"></span></a>
			</li>
			<li class="twitter">
				<a href="" data-share-page="twitter" target="_blank"><span class="icon-twitter"></span></a>
			</li>
			<li class="googleplus">
				<a href="" data-share-page="googleplus" target="_blank"><span class="icon-googleplus"></span></a>
			</li>
		</ul>
	</div>
	<div class="footer-partner">
		<div class="container">
			<ul>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_oddset.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_coba.png">
					</a>
				</li>
				<li class="hidden-small">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_post.png">
					</a>
				</li>
				<li class="visible-small">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_post_small.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_adidas.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_coca_cola.png">
					</a>
				</li>
			</ul>
		</div>
	</div>
	<div class="footer-meta-links">
		<div class="container">
			<nav class="metalinks">
				<ul>
					<li>
						<a href="http://www.fussball.de/imprint">Impressum</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/contact">Kontakt</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/privacy">Datenschutz</a>
					</li>
				</ul>
				<ul>
					<li>
						<a href="http://www.fussball.de/terms.and.conditions">Nutzungsbedingungen</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/youth.protection">Jugendschutz</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/content.responsibility">Inhalteverantwortung</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/cookie.settings">Cookies</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/">FAQ</a>
					</li>
				</ul>
			</nav>
			<div class="copyright">&copy; DFB</div>
		</div>
	</div>
	<div class="footer-slogan" data-adjust-footer-slogan-height>
		<div class="container"><span class="footer-slogan-text">Die Heimat des Amateurfussballs</span><span class="footer-slogan-logo"><img src="http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/font/logo.svg" alt="" width="24" class="logo-graphic" height="16"><span class="logo-letters">fussball.de</span></span></div>
	</div>
</footer>
		
		
	<div data-ajaxsurvey="//www.fussball.de/ajax.survey/-/path/_path_" data-survey-path-variable="_path_" data-survey="survey-1" id="ajax-survey"></div>
		


		
		<script type="text/javascript" nonce="" src="//www.fussball.de/static/por/6.80.99.3077/js/script.js"></script>
		
		<data-enable-tracking></data-enable-tracking>
	</body>
</html>
'''

ahtml = '''<!doctype html>
<html class="no-js">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		
		
		<title>FC Astoria Walldorf 2 (B-Junioren)</title>
		<meta name="default_image_title" content=""/>
		<link rel="canonical" href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" />
		<meta name="description" content="Alle Informationen zu den B-Junioren II des Vereins FC Astoria Walldorf"/>
		<meta name="keywords" content=""/>
		<meta name="robots" content="NOINDEX,FOLLOW"/>
		<meta name="generator" content=""/>
		<meta name="twitter:card" content="summary"/>
		<meta name="twitter:description" content="Alle Informationen zu den B-Junioren II des Vereins FC Astoria Walldorf"/>
		<meta name="twitter:image" content="http://www.fussball.de/export.media/-/action/getSocialMediaImage/page/mannschaft/team-id/011MIDI43O000000VTVG0001VTR8C1K7"/>
		<meta name="twitter:title" content="FC Astoria Walldorf 2 (B-Junioren)"/>
		<meta property="og:title" content="FC Astoria Walldorf 2 (B-Junioren)"/>
		<meta property="og:image" content="http://www.fussball.de/export.media/-/action/getSocialMediaImage/page/mannschaft/team-id/011MIDI43O000000VTVG0001VTR8C1K7"/>
		<meta property="og:image:width" content="600"/>
		<meta property="og:image:height" content="315"/>
		<meta property="og:url" content="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7"/>
		<meta property="og:type" content="website"/>
		<meta property="og:description" content="Alle Informationen zu den B-Junioren II des Vereins FC Astoria Walldorf"/>

		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

		<link rel="shortcut icon" type="image/x-icon" href="//www.fussball.de/static/por/6.80.99.3077/icon/favicon.ico" />
        <link rel="apple-touch-icon-precomposed" href="//www.fussball.de/static/por/6.80.99.3077/images/apple-touch-icon-precomposed.png">

		<link rel="stylesheet" href="//www.fussball.de/static/por/6.80.99.3077/css/style.css" />

		<!-- components::script_open_app -->

    <script type="text/javascript" nonce="">
      if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i))) {
        var headTag = document.getElementsByTagName("head")[0];
        var metaTag = document.createElement('meta');
        metaTag.name = 'apple-itunes-app';
        metaTag.content = 'app-id=901148836';
        headTag.appendChild(metaTag);
      }
    </script>

<!-- /components::script_open_app -->


		<script type="text/javascript" nonce="" src="//www.fussball.de/static/por/6.80.99.3077/js/lib/modernizr.min.js"></script>
			
		
		

	
		<script type="text/javascript" src="//assets.adobedtm.com/f1da398c27214bec64e7aa593c5a00f226037c10/satelliteLib-c17ea2874a9aa84b093067b5d761512b57eb0605.js"></script>
<script type="text/javascript">/*<![CDATA[*/(function(l,o,a,d,i,n,g,w,e,b){
g='AccengageWebSDKObject';w='script';l[g]=l[g]||{};l[g][n]=d;
l[d]=l[d]||[];l[d].p={'date':1*new Date(),'window':l,'document':o,'params':a};
e=o.createElement(w);b=o.getElementsByTagName(w)[0];e.async=1;
e.src='https://'+n+i+'/init.js';b.parentNode.insertBefore(e,b);
})(window,document,{},'ACC','/pushweb/assets','fussball-de-by.accengage.net');/*]]>*/</script>
<!-- Steps see adition docs -->
<!-- Step 1. load helper lib -->
<script type="text/javascript" src="http://www.fussball.de/static/por/6.80.99.3077/js/lib/wmConfig.min.js"></script>
<!-- 2. load ad lib -->
<script type="text/javascript">/*<![CDATA[*/var adition = adition || {};adition.srq = adition.srq || [];(function() {var script = document.createElement("script");script.type = "text/javascript";script.src = (document.location.protocol === "https:" ? "https:" : "http:") + "//imagesrv.adition.com/js/srp.js";script.charset = "utf-8";script.async =true;var firstScript = document.getElementsByTagName("script")[0];firstScript.parentNode.insertBefore(script, firstScript);})();/*]]>*/</script>
<!-- 3. register ad farm -->
<script type="text/javascript">/*<![CDATA[*/wmConfig.initConnection();wmConfig.pushViewport();/*]]>*/</script>
<!-- 4. configure slots, load and render -->
<script type="text/javascript">/*<![CDATA[*/if (wmConfig.existsApiLibrary()) {adition.srq.push(function(api) {
api.setProfile('Verband','32');
api.setProfile('Mannschaftsart','6');
api.setProfile('Plz','69190');
});}/*]]>*/</script>
<script type="text/javascript">/*<![CDATA[*/
wmConfig.pushConfig('slot-2895478',2895478);
wmConfig.pushConfig('slot-3688415',3688415);
wmConfig.pushConfig('slot-2895476',2895476);
wmConfig.pushConfig('slot-2895462',2895462);
wmConfig.loadAndRender();/*]]>*/</script>

		<script type="text/javascript">/*<![CDATA[*/
edArtikelId='';
edArtikelKategorie='';
edArtikelSchluesselwoerter='';
edArtikelTitel='';
edChannel='vereine_verbaende';
edGastmannschaftId='';
edGastmannschaftName='';
edGebiet='0123456789ABCDEF0123456700004180';
edGebietName='Baden';
edHeimmannschaftId='';
edHeimmannschaftName='';
edMandant='32';
edMannschaftId='011MIDI43O000000VTVG0001VTR8C1K7';
edMannschaftName='FC Astoria Walldorf 2';
edMannschaftsart='';
edMannschaftsartId='230';
edMannschaftsartName='B-Junioren';
edMannschaftsartTypId='6';
edMannschaftsartTypName='B-Junioren';
edSaison='0201IGL94G000000VS54898DVUL01S6C';
edSeite='mannschaft/-/saison/0201IGL94G000000VS54898DVUL01S6C/team-id/011MIDI43O000000VTVG0001VTR8C1K7';
edSeitennameKurz='mannschaft';
edSeitennameLang='mannschaft';
edSpielId='';
edSpielgebietId='';
edSpielgebietName='';
edSpielklasse='';
edSpielklasseId='';
edSpielklasseName='';
edSpielklasseTypId='';
edSpielklasseTypName='';
edSubchannel='';
edTickerId='';
edVerbandId='0123456789ABCDEF0123456700004180';
edVerbandName='Baden';
edVereinId='00ES8GN9B8000083VV0AG08LVUPGND5I';
edVereinName='FC Astoria Walldorf';
edVideoId='';
edVideoTitle='';
edWettbewerbId='';
edWettbewerbName='';
edWettkampfTyp='';
edWettkampfTypName='';
edWidgetTyp='';
fbedExtMa='';
fbedExtPlzMultiSpielst='';
fbedExtPlzMultiVerein='';
fbedExtPlzSpielst='69190';
fbedExtPlzVerein='69190';
fbedTeamTypeName='';
fbedWidgetKey='';
trackingcountername='mannschaft.Baden.32025069.B-Junioren';
if (window.location.href.indexOf('#_=_') > 0) {
	window.location = window.location.href.replace(/#.*/, '');
}
/*]]>*/</script>


	</head>
	<body class="fbde xhead_sectionteamcompetitions xhead_basesectionteamsquad xhead_sectionteamachievements xhead_sectionteamtimeline xhead_sectionteamcourts xhead_sectionteamstage" data-ng-controller="ApplicationController" data-marketing-cookies data-click-tracking data-scroll-spy data-ng-cloak global-events data-obfuscation-stylesheet="//www.fussball.de/export.fontface/-/id/%ID%/type/css">
		<header data-ng-controller="FlyoutController" data-ng-class="{active:flyoutState.isOpen, 'active-layer':layerState.isOpen}">
	<nav class="header-meta-nav">
		<div class="container">
			<div class="metanav-left">
				<ul>
					<li>
						<a href="http://www.dfb.de" target="_blank">dfb.de</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://kampagne.dfb.de/unsere-amateure/" target="_blank">Amateurfußballkampagne</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://fanshop.dfb.de/" target="_blank">DFB-Fanshop</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://fanclub.dfb.de/index.php?id=2" target="_blank">Fan Club Nationalmannschaft</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate" target="_blank">Shop</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.dfb.de/tickets" target="_blank">Tickets</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/partner" target="_blank">Partner</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/" target="_blank">FAQ</a>
					</li>
				</ul>
				<div class="sponsor-text">FUSSBALL.DE wird präsentiert von</div>
			</div>
			<div class="metanav-right">
				<div class="sponsor">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/temp/sponsor.png">
					</a>
				</div>
				<a href="#!" id="editor-link" class="visible-full">
					<span>Link</span>
					<script type="text/javascript">document.addEventListener('DOMContentLoaded', function () {document.getElementById('editor-link').addEventListener('click', function doThings() { alert('/mannschaft/-/saison/0201IGL94G000000VS54898DVUL01S6C/team-id/011MIDI43O000000VTVG0001VTR8C1K7');});});</script>
					<div data-user-dependency="{'FBDE_COMMUNITY_IN':'equal'}" data-ajaxcontent-type="jsonp" data-user="{'FBDE_COMMUNITY_IN':'1'}" data-ajaxcontent="https://www.fussball.de/login.community"></div>
					<div data-user-dependency="{'FBDE_COMMUNITY_OUT':'equal'}" data-ajaxcontent-type="jsonp" data-user="{'FBDE_COMMUNITY_OUT':'1'}" data-ajaxcontent="https://www.fussball.de/logout.community"></div>
				</a>
			</div>
		</div>
	</nav>
	<div class="header-main-nav">
		<div class="container">
			<div class="logo-wrapper">
				<div id="logo">
					<a data-ng-click="onLogoClick($event)" href="http://www.fussball.de/homepage">
						<img src="http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/logo.svg" alt="logo" width="24" class="logo-graphic" height="16">
						<span class="logo-letters">fussball.de</span>
					</a>
				</div>
			</div>
			<nav class="secondary-nav">
				<ul>
					<li class="seondary-nav-toggle">
						<a data-ng-click="toggleVisibleMobile()"><span class="icon-toggle"></span></a>
					</li>
					<li>
						<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
							<div data-flyoutitem-identifier="#login">
								
								<span></span>
								<img data-user-interpolate="src" data-user-interpolate-tmpl="%FBDE_USER_THUMB%" alt="thumb" class="img-profile">
							</div>
						</div>
						<div data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">
							<a href="https://www.fussball.de/login?fw_url=http%3A%2F%2Fwww.fussball.de%2Fmannschaft%2Ffc-astoria-walldorf-2-fc-astoria-walldorf-baden%2F-%2Fsaison%2F0201IGL94G000000VS54898DVUL01S6C%2Fteam-id%2F011MIDI43O000000VTVG0001VTR8C1K7"><span class="icon-login"></span></a>
						</div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#search"><span class="icon-search"></span></div>
					</li>
				</ul>
			</nav>
			<nav data-ng-class="{active: isVisibleMobile, hidden: scopeEnv.isMainMenuHidden}" class="primary-nav">
				<ul class="fast">
					<li>
						<a href="https://www.fussball.de/favorites"><span class="icon-favorits"></span>Favoriten</a>
					</li>
					<li>
						<a href="http://www.fussball.de/matchkalender"><span class="icon-matchcal"></span>Matchkalender</a>
					</li>
					<li>
						<div data-flyoutnavitem="main">
							<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-flyoutitem-identifier="#login">
								
								<span></span>
								<img data-user-interpolate="src" data-user-interpolate-tmpl="%FBDE_USER_THUMB%" alt="thumb" class="img-profile">
								<span data-user-interpolate="innerHTML" data-user-interpolate-tmpl="%FBDE_NICKNAME%"></span>
							</div>
						</div>
						<div data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">
							<a href="https://www.fussball.de/login?fw_url=http%3A%2F%2Fwww.fussball.de%2Fmannschaft%2Ffc-astoria-walldorf-2-fc-astoria-walldorf-baden%2F-%2Fsaison%2F0201IGL94G000000VS54898DVUL01S6C%2Fteam-id%2F011MIDI43O000000VTVG0001VTR8C1K7"><span class="icon-login"></span>Anmelden</a>
						</div>
					</li>
					<li data-flyoutnavitem="main">
						<div data-flyoutitem-identifier="#search"><span></span>Suche<span class="icon-search"></span></div>
					</li>
				</ul>
				<ul class="main">
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#flyout-news">News<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#competitions">Ligen<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}" class="active">
						<div data-flyoutitem-identifier="#pros">Vereine & Verbände<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#trainings">Training & Service<span class="icon-angle-right"></span></div>
					</li>
					<li data-flyoutnavitem="main" data-ng-class="{'current':isCurrent}">
						<div data-flyoutitem-identifier="#tv">Videos & Foren<span class="icon-angle-right"></span></div>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate/" target="_blank">Shop<span class="icon-angle-right"></span></a>
					</li>
				</ul>
				<ul class="meta">
					<li>
						<a href="http://www.dfb.de" target="_blank">dfb.de<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://kampagne.dfb.de/unsere-amateure/" target="_blank">Amateurfußballkampagne<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://fanshop.dfb.de/" target="_blank">DFB-Fanshop<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://fanclub.dfb.de/index.php?id=2" target="_blank">Fan Club Nationalmannschaft<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="https://www.outfitter.de/fbde/?utm_source=fussballde&utm_medium=affiliate" target="_blank">Shop<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://www.dfb.de/tickets" target="_blank">Tickets<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://www.fussball.de/partner" target="_blank">Partner<span class="icon-link-arrow"></span></a>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/" target="_blank">FAQ<span class="icon-link-arrow"></span></a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
	<div data-user-favorites-load-cookie="FBDE_USER_ID" data-ng-class="{'opened':flyoutState.isOpen}" id="header-flyout" class="header-flyout" data-user-favorites-load="https://www.fussball.de/ajax.favorites">
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="flyout-news" class="flyout-subnav">
			<div class="container">
				<div data-ng-controller="ToolboxController" class="news-list-toolbox news-list-toolbox-menu" data-toolbox>
					<div class="flyout-left">
						<nav class="flyout-nav">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>News</h4>
							<ul>
								<li data-toolbox-value="all_news" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/all_news">
									<div><span></span>Alle<span></span></div>
								</li>
								<li data-toolbox-value="magazin" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/magazin">
									<div><span></span>Magazin<span></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="regional-league-categories">
									<div data-flyoutitem-identifier="#regional-league-categories"><span></span>Regionalliga<span class="icon-angle-right"></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="association-categories">
									<div data-flyoutitem-identifier="#association-categories"><span></span>Verbände<span class="icon-angle-right"></span></div>
								</li>
								<li data-toolbox-value="service" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/service">
									<div><span></span>Service<span></span></div>
								</li>
								<li data-toolbox-value="aktionen" data-toolbox-headermenu-item="single" data-ng-class="{'current':isCurrent}" data-toolbox-key="include" data-toolbox-target="http://www.fussball.de/news/-/include/aktionen">
									<div><span></span>Aktionen<span></span></div>
								</li>
								<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}" data-toolbox-flyout-right="helpcenter-categories">
									<div data-flyoutitem-identifier="#helpcenter-categories"><span></span>Hilfe-Center<span class="icon-angle-right"></span></div>
								</li>
							</ul>
						</nav>
					</div>
					<div class="flyout-right">
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="helpcenter-categories" class="flyout-tab">
							<div data-flyout-content=".filter-helpcenter" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-helpcenter-categories" data-toolbox-key="helpcenter-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Hilfe-Center<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/helpcenter" data-toolbox-key="helpcenter-categories" class="filter-categories filter-assoc filter-helpcenter">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Hilfe-Center
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11198">
													<strong>Allgemeines</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11199">
													<strong>APP</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11200">
													<strong>Liveticker</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11201">
													<strong>Mannschaftsseite</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11202">
													<strong>Profile</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11203">
													<strong>Registrierung</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11204">
													<strong>Training & Service</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11205">
													<strong>Widgets</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="regional-league-categories" class="flyout-tab">
							<div data-flyout-content=".filter-regionalliga" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-regional-league-categories" data-toolbox-key="regional-league-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Regionalliga<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/regionalliga" data-toolbox-key="regional-league-categories" class="filter-categories filter-assoc filter-regionalliga">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Regionalligen
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11212">
													<strong>Regionalliga Nord</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11213">
													<strong>Regionalliga Nordost</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11211">
													<strong>Regionalliga West</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11209">
													<strong>Regionalliga Südwest</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11210">
													<strong>Regionalliga Bayern</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
						<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="association-categories" class="flyout-tab">
							<div data-flyout-content=".filter-verband" data-toolbox-flyout-header-menu="filterList" id="link-flyout-right-association-categories" data-toolbox-key="association-categories"></div>
							<div class="container">
								<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;">Verbände<span class="icon-angle-left"></span></h4>
								<div data-toolbox-headermenu-item="list" data-toolbox-target="http://www.fussball.de/news/-/include/verbaende" data-toolbox-key="association-categories" class="filter-categories filter-assoc filter-verband">
									<div data-ng-class="{'on': showSelectList}" data-ng-click="showSelectList = !showSelectList" class="select-wrapper-toolbox">
										<div tabindex="0" class="selection visible-small">
											<div class="value">Verbände
												<strong class="currentSelection" data-attr-selection-info></strong>
											</div>
											<span class="icon-angle-down"></span>
										</div>
										<ul class="list select-list">
											<li class="visible-small">
												<label data-checkbox="" class="checkbox">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
													<strong data-attr-select-all-label>Alle Auswählen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11032">
													<div class="logo hidden-small"><span data-alt="Baden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004180"></span></div>
													<strong>Baden</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11031">
													<div class="logo hidden-small"><span data-alt="Bayern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/00ES8GNCQK000000VV0AG08LVUPGND5I"></span></div>
													<strong>Bayern</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11066">
													<div class="logo hidden-small"><span data-alt="Berlin" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004240"></span></div>
													<strong>Berlin</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11061">
													<div class="logo hidden-small"><span data-alt="Brandenburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004250"></span></div>
													<strong>Brandenburg</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11002">
													<div class="logo hidden-small"><span data-alt="Bremen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004090"></span></div>
													<strong>Bremen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11003">
													<div class="logo hidden-small"><span data-alt="Hamburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004080"></span></div>
													<strong>Hamburg</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11034">
													<div class="logo hidden-small"><span data-alt="Hessen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004170"></span></div>
													<strong>Hessen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11062">
													<div class="logo hidden-small"><span data-alt="Mecklenburg-Vorpommern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004220"></span></div>
													<strong>Mecklenburg-Vorpommern</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11023">
													<div class="logo hidden-small"><span data-alt="Mittelrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004120"></span></div>
													<strong>Mittelrhein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11022">
													<div class="logo hidden-small"><span data-alt="Niederrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004110"></span></div>
													<strong>Niederrhein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11001">
													<div class="logo hidden-small"><span data-alt="Niedersachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004100"></span></div>
													<strong>Niedersachsen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11041">
													<div class="logo hidden-small"><span data-alt="Rheinland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004140"></span></div>
													<strong>Rheinland</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11043">
													<div class="logo hidden-small"><span data-alt="Saarland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004150"></span></div>
													<strong>Saarland</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11063">
													<div class="logo hidden-small"><span data-alt="Sachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004270"></span></div>
													<strong>Sachsen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11064">
													<div class="logo hidden-small"><span data-alt="Sachsen-Anhalt" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004230"></span></div>
													<strong>Sachsen-Anhalt</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11004">
													<div class="logo hidden-small"><span data-alt="Schleswig-Holstein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004070"></span></div>
													<strong>Schleswig-Holstein</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11033">
													<div class="logo hidden-small"><span data-alt="Südbaden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004190"></span></div>
													<strong>Südbaden</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11042">
													<div class="logo hidden-small"><span data-alt="Südwest" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004160"></span></div>
													<strong>Südwest</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11065">
													<div class="logo hidden-small"><span data-alt="Thüringen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004260"></span></div>
													<strong>Thüringen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11021">
													<div class="logo hidden-small"><span data-alt="Westfalen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004130"></span></div>
													<strong>Westfalen</strong>
												</label>
											</li>
											<li>
												<label data-checkbox="" class="checkbox" data-attr-select-option="true">
													<span class="icon-verified"></span>
													<input name="filter-items" data-attr-toggle-type="single" checked="checked" type="checkbox" value="11035">
													<div class="logo hidden-small"><span data-alt="Württemberg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004200"></span></div>
													<strong>Württemberg</strong>
												</label>
											</li>
										</ul>
									</div>
									<div class="general">
										<div class="hidden-small">
											<label data-checkbox="" class="checkbox">
												<span class="icon-verified"></span>
												<input name="filter-items" data-attr-toggle-type="all" checked="checked" type="checkbox" value="true">
												<strong data-attr-select-all-label>Alle Auswählen</strong>
											</label>
										</div>
										<button type="submit" class="button button-primary">Los</button>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="competitions" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Ligen</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#wam"><span></span>Alle Ligen<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#topleagues"><span></span>Top-Ligen<span class="icon-angle-right"></span></div>
							</li>
							<li data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-ng-class="{'current':isCurrent}">
								<a href="https://www.fussball.de/account.matchplan.next">Dein Spielplan</a>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#stats"><span></span>Amateurstatistiken<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#matchcal"><span></span>Matchkalender<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="wam" class="flyout-tab">
						<div class="wam header-flyout-wam">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Wettbewerbsauswahl</h4>
							<div class="inner">
								<form method="GET" data-url-submit="" data-url-competitions="//www.fussball.de/wam_wettbewerbsurls_CLIENT_SEASON_COMPETITIONTYPE_TEAMTYPE.json" data-url-base="//www.fussball.de/wam_base.json" data-url-areas="//www.fussball.de/wam_arten_CLIENT_SEASON_COMPETITIONTYPE.json" data-wam>
									<div class="form-wrapper">
										<div data-ng-class="{on: wamData.clients.isOpen, cta: wamData.clients.isCta, disabled: wamData.clients.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.clients.length == 1 || clickHandler(0)" class="selection">
												<div data-ng-bind="wamData.clientsSelected.label || 'Verband wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.clients" data-ng-class="{on: wamData.clientsSelected.id == option.id}">
													<a data-ng-click="wamData.clients.isOpen = !wamData.clients.isOpen; wamData.clientsSelected = option; wamUpdate('clients',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.clientsSelected" size="1" data-ng-disabled="wamData.clients.length == 1" name="clients" data-ng-change="onChange()" data-label="Verband wählen" data-ng-options="option as option.label for option in wamData.clients track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.seasons.isOpen, cta: wamData.seasons.isCta, disabled: wamData.seasons.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.seasons.length == 1 || clickHandler(1)" class="selection">
												<div data-ng-bind="wamData.seasonsSelected.label || 'Saison wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.seasons" data-ng-class="{on: wamData.seasonsSelected.id == option.id}">
													<a data-ng-click="wamData.seasons.isOpen = !wamData.seasons.isOpen; wamData.seasonsSelected = option; wamUpdate('seasons',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.seasonsSelected" size="1" data-ng-disabled="wamData.seasons.length == 1" name="seasons" data-ng-change="onChange()" data-label="Saison wählen" data-ng-options="option as option.label for option in wamData.seasons track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.competitionTypes.isOpen, cta: wamData.competitionTypes.isCta, disabled: wamData.competitionTypes.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.competitionTypes.length == 1 || clickHandler(2)" class="selection">
												<div data-ng-bind="wamData.competitionTypesSelected.label || 'Typ wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.competitionTypes" data-ng-class="{on: wamData.competitionTypesSelected.id == option.id}">
													<a data-ng-click="wamData.competitionTypes.isOpen = !wamData.competitionTypes.isOpen; wamData.competitionTypesSelected = option; wamUpdate('competitionTypes',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.competitionTypesSelected" size="1" data-ng-disabled="wamData.competitionTypes.length == 1" name="competitionTypes" data-ng-change="onChange()" data-label="Typ wählen" data-ng-options="option as option.label for option in wamData.competitionTypes track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.teamTypes.isOpen, cta: wamData.teamTypes.isCta, disabled: wamData.teamTypes.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.teamTypes.length == 1 || clickHandler(3)" class="selection">
												<div data-ng-bind="wamData.teamTypesSelected.label || 'Mannschaftsart wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.teamTypes" data-ng-class="{on: wamData.teamTypesSelected.id == option.id}">
													<a data-ng-click="wamData.teamTypes.isOpen = !wamData.teamTypes.isOpen; wamData.teamTypesSelected = option; wamUpdate('teamTypes',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.teamTypesSelected" size="1" data-ng-disabled="wamData.teamTypes.length == 1" name="teamTypes" data-ng-change="onChange()" data-label="Mannschaftsart wählen" data-ng-options="option as option.label for option in wamData.teamTypes track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.leagues.isOpen, cta: wamData.leagues.isCta, disabled: wamData.leagues.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.leagues.length == 1 || clickHandler(4)" class="selection">
												<div data-ng-bind="wamData.leaguesSelected.label || 'Spielklasse wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.leagues" data-ng-class="{on: wamData.leaguesSelected.id == option.id}">
													<a data-ng-click="wamData.leagues.isOpen = !wamData.leagues.isOpen; wamData.leaguesSelected = option; wamUpdate('leagues',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.leaguesSelected" size="1" data-ng-disabled="wamData.leagues.length == 1" name="leagues" data-ng-change="onChange()" data-label="Spielklasse wählen" data-ng-options="option as option.label for option in wamData.leagues track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.areas.isOpen, cta: wamData.areas.isCta, disabled: wamData.areas.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.areas.length == 1 || clickHandler(5)" class="selection">
												<div data-ng-bind="wamData.areasSelected.label || 'Gebiet wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.areas" data-ng-class="{on: wamData.areasSelected.id == option.id}">
													<a data-ng-click="wamData.areas.isOpen = !wamData.areas.isOpen; wamData.areasSelected = option; wamUpdate('areas',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.areasSelected" size="1" data-ng-disabled="wamData.areas.length == 1" name="areas" data-ng-change="onChange()" data-label="Gebiet wählen" data-ng-options="option as option.label for option in wamData.areas track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
										<div data-ng-class="{on: wamData.competitions.isOpen, cta: wamData.competitions.isCta, disabled: wamData.competitions.length == 1}" class="select-wrapper">
											<div data-ng-click="wamData.competitions.length == 1 || clickHandler(6)" class="selection">
												<div data-ng-bind="wamData.competitionsSelected.label || 'Wettbewerb wählen'" class="value"></div>
												<span class="icon-angle-down"></span>
											</div>
											<ul class="select-list">
												<li data-ng-repeat="option in wamData.competitions" data-ng-class="{on: wamData.competitionsSelected.id == option.id}">
													<a data-ng-click="wamData.competitions.isOpen = !wamData.competitions.isOpen; wamData.competitionsSelected = option; wamUpdate('competitions',$index)">{{option.label}}</a>
												</li>
											</ul>
											<div class="select">
												<select data-ng-model="wamData.competitionsSelected" size="1" data-ng-disabled="wamData.competitions.length == 1" name="competitions" data-ng-change="onChange()" data-label="Wettbewerb wählen" data-ng-options="option as option.label for option in wamData.competitions track by option.id" data-wam-select>
													<option data-ng-if="false" value=""></option>
												</select>
											</div>
										</div>
									</div>
									<div data-user-favorites-save="https://www.fussball.de/add.favorite">
										<a data-user-dependency="{'FBDE_USER_ID':'exist'}" data-ng-click="saveFavorite(wamData.competitionsSelected)" data-ng-class="{'disabled':!wamData.competitionsSelected.id}" class="button button-primary favorits trigger-login-layer">als Favorit speichern</a>
									</div>
									<div class="form-submit" data-wam-submit>
										<button data-ng-click="submitForm()" data-ng-class="{'disabled':!wamData.competitionsSelected.id}" type="submit" class="button button-primary">Anzeigen</button>
									</div>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="competitions" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="topleagues" class="flyout-tab">
						<div class="header-flyout-wam header-flyout-link-list wam">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Top-Ligen Herren 17/18</h4>
							<div class="inner">
								<h3 class="hidden-small">Herren 17/18</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/bundesliga-deutschland-bundesliga-herren-saison1718-deutschland/-/staffel/01VM7AT5SK000001VS54898EVSV90M3P-G" class="link">Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2bundesliga-deutschland-2bundesliga-herren-saison1718-deutschland/-/staffel/01VV7REICS00000DVS54898DVTPALDN0-G" class="link">2.Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/3liga-deutschland-3liga-herren-saison1718-deutschland/-/staffel/01VM7AUE1K000000VS54898EVSV90M3P-G" class="link">3.Liga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-nord-region-norddeutschland-regionalliga-herren-saison1718-region-norddeutschland/-/staffel/01VON662IK000000VS54898DVT75CK91-G" class="link">Regionalliga Nord<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-nordost-region-nordostdeutschland-regionalliga-herren-saison1718-region-nordostdeutschland/-/staffel/0204BP0IA8000004VS54898EVSIMIKOR-G" class="link">Regionalliga Nordost<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-suedwest-region-suedwestdeutschland-regionalliga-herren-saison1718-region-suedwestdeutschland/-/staffel/0201G63B98000001VS54898EVSIMIKOR-G" class="link">Regionalliga Südwest<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-west-region-westdeutschland-regionalliga-herren-saison1718-region-westdeutschland/-/staffel/01VVHJ6FSG00000AVS54898DVUL01S6C-G" class="link">Regionalliga West<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/regionalliga-bayern-bayern-regionalliga-bayern-herren-saison1718-bayern/-/staffel/0200TN5NS0000007VS54898DVUL01S6C-G" class="link">Regionalliga Bayern<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/dfb-pokal-deutschland-dfb-pokal-herren-saison1718-deutschland/-/staffel/01VUJJCMU4000000VS54898DVTPALDN0-C" class="link">DFB-Pokal<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
						<div class="header-flyout-wam header-flyout-link-list profiles">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Top-Ligen Frauen 17/18</h4>
							<div class="inner">
								<h3 class="hidden-small">Frauen 17/18</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/allianz-frauen-bundesliga-deutschland-bundesliga-frauen-saison1718-deutschland/-/staffel/020C461154000001VS54898EVVNLA7IG-G" class="link">Allianz Frauen-Bundesliga<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2-frauen-bundesliga-nord-deutschland-2bundesliga-frauen-saison1718-deutschland/-/staffel/01VM7B7SQC000002VS54898EVSV90M3P-G" class="link">2. Frauen-Bundesliga Nord<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/2-frauen-bundesliga-sued-deutschland-2bundesliga-frauen-saison1718-deutschland/-/staffel/01VM7B7T4C000006VS54898EVSV90M3P-G" class="link">2. Frauen-Bundesliga Süd<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/spieltagsuebersicht/dfb-pokal-frauen-deutschland-dfb-pokal-frauen-saison1718-deutschland/-/staffel/020A3KANFG000000VS54898DVUVCCN5J-C" class="link">DFB-Pokal Frauen<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="matchcal" class="flyout-tab">
						<div class="matchcal header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Matchkalender</h4>
							<div class="inner form-dark">
								<h3>Begegnungen in deiner Nähe</h3>
								<form method="GET" action="//www.fussball.de/matchkalender" data-rest-form>
									<div data-ng-controller="TypeaheadController" data-typeahead="http://www.fussball.de/public.service/-/action/getPostalCodeCompletions" data-typeahead-minlength="3" data-typeahead-key="plz" class="label-wrapper location" data-typeahead-type="noselect" data-typeahead-default="{'action':'getPostalCodeCompletions'}">
										<div class="typeahead-wrapper">
											<label for="matchplan-calendar-location">Umgebung:</label>
											<input data-ng-model="typeaheadInput.text" name="plz" data-ng-change="updateInput()" data-ng-show="!showSelected()" placeholder="PLZ / Ort*" id="matchplan-calendar-location" type="text" value="" data-ajaxmodel="plz">
											<ul data-ng-class="{'on':isActiveList()}" class="typeahead-list">
												<li data-ng-show="isActiveError()"><span>Keine Postleitzahlen gefunden. Bitte überprüfe deine Angabe.</span></li>
												<li data-ng-repeat="item in filterResults('$', typeaheadItems, typeaheadInput.text)" data-ng-class-even="'even'" data-ng-show="isActiveResults()">
													<a data-ng-click="chooseItem(item, 'postalCode')" href="">{{item.postalCode}}, {{item.city}}</a>
												</li>
											</ul>
											<p data-ng-show="showSelected()" class="typeahead-selected">
												{{typeaheadInput.text}}
												<a data-ng-click="resetSelected()" href="" class="close"><span class="icon-close"></span></a>
											</p>
										</div>
									</div>
									<div class="cal-group">
										<div class="datepicker-wrapper">
											<div data-calendar-type="from" data-calendar-span="14" data-ng-controller="MatchcalController" class="date datepicker label-wrapper">
												<label for="matchcal-date-from">Von:</label>
												<input data-ng-model="dt" data-ng-init="dt='2018-04-11'" name="datum-von" data-datepicker-popup="dd.MM.yyyy" data-is-open="opened" placeholder="Datum*" id="matchcal-date-from" type="text" value="" data-ajaxmodel="datum-von">
												<label for="matchcal-date-from" data-ng-class="{'open':opened}"><span class="icon-matchcal"></span></label>
											</div>
										</div>
										<div class="datepicker-wrapper">
											<div data-calendar-type="to" data-calendar-span="14" data-ng-controller="MatchcalController" class="date datepicker label-wrapper">
												<label for="matchcal-date-to">Bis:</label>
												<input data-ng-model="dt" data-ng-init="dt='2018-04-25'" name="datum-bis" data-datepicker-popup="dd.MM.yyyy" data-is-open="opened" placeholder="Datum*" id="matchcal-date-to" type="text" value="" data-ajaxmodel="datum-bis">
												<label for="matchcal-date-to" data-ng-class="{'open':opened}"><span class="icon-matchcal"></span></label>
											</div>
										</div>
									</div>
									<div data-ng-model="filterCompetitions" data-select-box="single" data-select-box-default="0" data-select-title="Wettbewerbe" class="select-wrapper" data-ajaxmodel="wettkampftyp">
										<select size="1" name="wettkampftyp">
											<option value="-1">Alle</option>
											<option value="1">Meisterschaften</option>
											<option value="8">Pokale</option>
											<option value="3">Turniere</option>
											<option value="7">Freundschaftsspiele</option>
											<option value="6">Privatspiele</option>
											<option value="9">Auswahlspiele</option>
											<option value="11">Futsal-Ligabetrieb</option>
											<option value="2">Hallenturniere (Futsal)</option>
										</select>
									</div>
									<div data-ng-model="filterTeams" data-select-box="multiple" data-select-box-default="0" data-select-title="Mannschaften" class="select-wrapper" data-ajaxmodel="mannschaftsart" data-select-box-multiple="ausgewählt">
										<select size="1" name="mannschaftsart" multiple>
											<option value="-1">Alle</option>
											<option value="1">Herren</option>
											<option value="39">Herren-Reserve</option>
											<option value="54">Herren - Behindertenfußball</option>
											<option value="807">Senioren Ü60 Freizeit/Betrieb</option>
											<option value="809">Senioren Ü50 Freizeit/Betrieb</option>
											<option value="811">Senioren Ü40 Freizeit/Betrieb</option>
											<option value="812">Senioren Ü32 Freizeit/Betrieb</option>
											<option value="813">Herren Freizeit/Betrieb</option>
											<option value="3">A-Junioren</option>
											<option value="6">B-Junioren</option>
											<option value="8">C-Junioren</option>
											<option value="10">D-Junioren</option>
											<option value="12">E-Junioren</option>
											<option value="14">F-Junioren</option>
											<option value="16">G-Junioren</option>
											<option value="19">Altherren</option>
											<option value="20">Alt-Senioren</option>
											<option value="21">Alte Herren Ü50</option>
											<option value="24">Altliga Ü50</option>
											<option value="23">Altliga Ü60</option>
											<option value="47">Alte Herren Ü60</option>
											<option value="49">Altliga Ü70</option>
											<option value="55">Seniorinnen Ü35</option>
											<option value="48">Seniorinnen Ü30</option>
											<option value="4">Frauen</option>
											<option value="5">A-Juniorinnen</option>
											<option value="7">B-Juniorinnen</option>
											<option value="9">C-Juniorinnen</option>
											<option value="11">D-Juniorinnen</option>
											<option value="13">E-Juniorinnen</option>
											<option value="15">F-Juniorinnen</option>
											<option value="17">G-Juniorinnen</option>
											<option value="22">Freizeitsport</option>
											<option value="40">Freizeitsport Frauen</option>
										</select>
									</div>
									<button type="submit" class="button button-primary button-block">Suchen</button>
									<p class="mandatory">* Pflichtfelder</p>
								</form>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="stats" class="flyout-tab">
						<div class="stats header-flyout-stats">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Amateurstatistiken</h4>
							<div class="inner">
								<h3>Deutschlands Beste</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/stats.amateur.team/-/mandantspez/false/stats/4"><span class="icon-team-logo"></span><span class="link">Bestes Team<span class="icon-link-arrow"></span></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/stats.amateur.player/-/mandantspez/false/stats/8"><span class="icon-player-image"></span><span class="link">Bester Stürmer<span class="icon-link-arrow"></span></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/stats.amateur.team/-/mandantspez/false/stats/5"><span class="icon-soccer-ball"></span><span class="link">Alle Top-Statistiken<span class="icon-link-arrow"></span></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="pros" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Vereine & Verbände</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#region"><span></span>Regionalverbände<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#fed"><span></span>Landesverbände<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#searchAssociation"><span></span>Vereine<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#searchPlayer"><span></span>Spieler<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="region" class="flyout-tab">
						<div class="region header-flyout-associations">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Regionalverbände</h4>
							<div class="inner">
								<div class="block">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/regionalverband/region-norddeutschland/-/verband/0123456789ABCDEF0123456700004020" class="association-wrapper">
												<div class="logo"><span data-alt="Region Norddeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004020"></span></div>
												<div class="name">Norddeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-nordostdeutschland/-/verband/0123456789ABCDEF0123456700004060" class="association-wrapper">
												<div class="logo"><span data-alt="Region Nordostdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004060"></span></div>
												<div class="name">Nordostdeutscher Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-sueddeutschland/-/verband/0123456789ABCDEF0123456700004050" class="association-wrapper">
												<div class="logo"><span data-alt="Region Süddeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004050"></span></div>
												<div class="name">Süddeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
								<div class="block last">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/regionalverband/region-suedwestdeutschland/-/verband/0123456789ABCDEF0123456700004040" class="association-wrapper">
												<div class="logo"><span data-alt="Region Südwestdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004040"></span></div>
												<div class="name">Fußball-Regional-Verband Südwest<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/regionalverband/region-westdeutschland/-/verband/0123456789ABCDEF0123456700004030" class="association-wrapper">
												<div class="logo"><span data-alt="Region Westdeutschland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004030"></span></div>
												<div class="name">Westdeutscher Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="fed" class="flyout-tab">
						<div class="fed header-flyout-associations">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Landesverbände</h4>
							<div class="inner">
								<div class="block">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180" class="association-wrapper">
												<div class="logo"><span data-alt="Baden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004180"></span></div>
												<div class="name">Badischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/bremen/-/verband/0123456789ABCDEF0123456700004090" class="association-wrapper">
												<div class="logo"><span data-alt="Bremen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004090"></span></div>
												<div class="name">Bremer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/mittelrhein/-/verband/0123456789ABCDEF0123456700004120" class="association-wrapper">
												<div class="logo"><span data-alt="Mittelrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004120"></span></div>
												<div class="name">Fußball-Verband Mittelrhein<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/saarland/-/verband/0123456789ABCDEF0123456700004150" class="association-wrapper">
												<div class="logo"><span data-alt="Saarland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004150"></span></div>
												<div class="name">Saarländischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/suedbaden/-/verband/0123456789ABCDEF0123456700004190" class="association-wrapper">
												<div class="logo"><span data-alt="Südbaden" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004190"></span></div>
												<div class="name">Südbadischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/wuerttemberg/-/verband/0123456789ABCDEF0123456700004200" class="association-wrapper">
												<div class="logo"><span data-alt="Württemberg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004200"></span></div>
												<div class="name">Württembergischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
									<ul class="col last">
										<li>
											<a href="http://www.fussball.de/verband/bayern/-/verband/00ES8GNCQK000000VV0AG08LVUPGND5I" class="association-wrapper">
												<div class="logo"><span data-alt="Bayern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/00ES8GNCQK000000VV0AG08LVUPGND5I"></span></div>
												<div class="name">Bayerischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/hamburg/-/verband/0123456789ABCDEF0123456700004080" class="association-wrapper">
												<div class="logo"><span data-alt="Hamburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004080"></span></div>
												<div class="name">Hamburger Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/niederrhein/-/verband/0123456789ABCDEF0123456700004110" class="association-wrapper">
												<div class="logo"><span data-alt="Niederrhein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004110"></span></div>
												<div class="name">Fußballverband Niederrhein e.V.<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/sachsen/-/verband/0123456789ABCDEF0123456700004270" class="association-wrapper">
												<div class="logo"><span data-alt="Sachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004270"></span></div>
												<div class="name">Sächsischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/suedwest/-/verband/0123456789ABCDEF0123456700004160" class="association-wrapper">
												<div class="logo"><span data-alt="Südwest" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004160"></span></div>
												<div class="name">Südwestdeutscher Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
								<div class="block last">
									<ul class="col">
										<li>
											<a href="http://www.fussball.de/verband/berlin/-/verband/0123456789ABCDEF0123456700004240" class="association-wrapper">
												<div class="logo"><span data-alt="Berlin" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004240"></span></div>
												<div class="name">Berliner Fußball-Verband e. V.<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/hessen/-/verband/0123456789ABCDEF0123456700004170" class="association-wrapper">
												<div class="logo"><span data-alt="Hessen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004170"></span></div>
												<div class="name">Hessischer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/niedersachsen/-/verband/0123456789ABCDEF0123456700004100" class="association-wrapper">
												<div class="logo"><span data-alt="Niedersachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004100"></span></div>
												<div class="name">Niedersächsischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/sachsen-anhalt/-/verband/0123456789ABCDEF0123456700004230" class="association-wrapper">
												<div class="logo"><span data-alt="Sachsen-Anhalt" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004230"></span></div>
												<div class="name">Fußballverband Sachsen-Anhalt<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/thueringen/-/verband/0123456789ABCDEF0123456700004260" class="association-wrapper">
												<div class="logo"><span data-alt="Thüringen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004260"></span></div>
												<div class="name">Thüringer Fußball-Verband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
									<ul class="col last">
										<li>
											<a href="http://www.fussball.de/verband/brandenburg/-/verband/0123456789ABCDEF0123456700004250" class="association-wrapper">
												<div class="logo"><span data-alt="Brandenburg" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004250"></span></div>
												<div class="name">Fußball-Landesverband Brandenburg<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/mecklenburg-vorpommern/-/verband/0123456789ABCDEF0123456700004220" class="association-wrapper">
												<div class="logo"><span data-alt="Mecklenburg-Vorpommern" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004220"></span></div>
												<div class="name">Landesfußballverband Mecklenburg-Vorpommern<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/rheinland/-/verband/0123456789ABCDEF0123456700004140" class="association-wrapper">
												<div class="logo"><span data-alt="Rheinland" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004140"></span></div>
												<div class="name">Fußballverband Rheinland<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/schleswig-holstein/-/verband/0123456789ABCDEF0123456700004070" class="association-wrapper">
												<div class="logo"><span data-alt="Schleswig-Holstein" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004070"></span></div>
												<div class="name">Schleswig-Holsteinischer Fußballverband<span class="icon-link-arrow"></span></div>
											</a>
										</li>
										<li>
											<a href="http://www.fussball.de/verband/westfalen/-/verband/0123456789ABCDEF0123456700004130" class="association-wrapper">
												<div class="logo"><span data-alt="Westfalen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/1/id/0123456789ABCDEF0123456700004130"></span></div>
												<div class="name">Fußball- u. Leichtathletik-Verband Westfalen<span class="icon-link-arrow"></span></div>
											</a>
										</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="searchAssociation" class="flyout-tab">
						<div class="search header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Vereine</h4>
							<div class="inner form-dark">
								<h3>Vereine nach Name und Region finden</h3>
								<form method="GET" action="//www.fussball.de/suche.verein" data-rest-form>
									<input data-ng-model="text" name="text" placeholder="Vereinsname*" type="text" value="">
									<div class="location label-wrapper">
										<label for="plz">Umgebung</label>
										<input data-ng-model="plz" name="plz" placeholder="PLZ / Ort*" id="flyout-search-club-zip" type="text" value="">
									</div>
									<button type="submit" class="button button-primary button-block">Finden</button>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="club" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="searchPlayer" class="flyout-tab">
						<div class="search header-flyout-form">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Spieler</h4>
							<div class="inner form-dark">
								<h3>Spieler nach Name und Region finden</h3>
								<form method="GET" action="//www.fussball.de/suche.spieler" data-rest-form>
									<input data-ng-model="firstname" name="firstname" placeholder="Vorname*" type="text" value="" class="small">
									<input data-ng-model="lastname" name="lastname" placeholder="Nachname*" type="text" value="" class="small">
									<div class="location label-wrapper">
										<label for="plz">Umgebung</label>
										<input data-ng-model="plz" name="plz" placeholder="PLZ / Ort*" id="flyout-search-player-zip" type="text" value="" class="small">
									</div>
									<button type="submit" class="button button-primary button-block">Finden</button>
								</form>
							</div>
						</div>
						<div class="favs header-flyout-favorites">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Favoriten</h3>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" data-user-favorites="player" class="user-favorites-load" data-lazyload></div>
									<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="favorits">
										<a href="https://www.fussball.de/favorites">Deine Favoriten<span class="icon-link-arrow"></span></a>
									</div>
								</div>
							</div>
							<p data-user-dependency="{'FBDE_USER_ID':'notexistVisible'}">Wenn Du dich bei unserer Community einloggst, kannst du Vereine und Mannschaften als Favoriten speichern und direkt von hier aus schnell und einfach erreichen.</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="trainings" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Training & Service</h4>
						<ul>
							<li data-ng-class="{'current':isCurrent}">
								<div>
									<a href="http://training-service.fussball.de/">Übersichtsseite<span></span></a>
								</div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings2">Trainer/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings3">Spieler/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings4">Lehrer/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings5">Schiedsrichter/in<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#trainings6">Vereinsmitarbeiter/in<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings2" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Trainer/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/trainer" class="link">Startseite Trainer/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/bambini" class="link">Bambini<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/f-juniorin" class="link">F-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/e-juniorin" class="link">E-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/d-juniorin" class="link">D-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/c-juniorin" class="link">C-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/b-juniorin" class="link">B-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/a-juniorin" class="link">A-Junior/-in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/aktiver-ue-20" class="link">Aktive/Ü 20<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/trainer/seniorin-ue-35" class="link">Senior/in Ü 35<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings3" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Spieler/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/spieler" class="link">Startseite Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/bis-u-11-spielerin" class="link">Bis U 11-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/u-12-bis-u-15-spielerin" class="link">U 12- bis U 15-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/u-16-bis-u-19-spielerin" class="link">U 16- bis U 19-Spieler/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/aktive-ue20" class="link">Aktive/r Ü 20<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/spieler/seniorin-ue-35" class="link">Senior/in Ü 35<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings4" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Lehrer/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/lehrer" class="link">Startseite Lehrer/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/lehrer/grundschule" class="link">Grundschule<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/lehrer/weiterfuehrende-schule" class="link">Weiterführende Schulen<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings5" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Schiedsrichter/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter" class="link">Startseite Schiedsrichter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/aktiver-schiedsrichterin" class="link">Aktive/r Schiedsrichter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/interessentin" class="link">Interessent/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/schiedsrichter/funktionaerin" class="link">Funktionär/in<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="trainings6" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Vereinsmitarbeiter/in</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter" class="link">Startseite Vereinsmitarbeiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/vereinsvorsitzender" class="link">Vereinsvorsitzende/r<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/abteilungsleiterin-fussball" class="link">Abteilungsleiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/jugendleiterin" class="link">Jugendleiter/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/schatzmeisterin" class="link">Schatzmeister/in<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://training-service.fussball.de/vereinsmitarbeiter/pressesprecherin" class="link">Pressereferent/in<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="tv" class="flyout-subnav">
			<div class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Videos & Foren</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv1">Amateur-TV<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv2">Fotos<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#tv3">Foren<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv1" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Amateur-TV</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/amateur.tv.magazin" class="link">Magazin<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/amateur.tv.voting/-/rubrik/zdftw" class="link">ZDF Torwandschießen<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/fan.video" class="link">Fanvideos<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv2" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Fotos</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/fan.photo" class="link">Fanfotos<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/fan.photo.alben" class="link">Fotoalben<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="tv3" class="flyout-tab">
						<div class="header-flyout-two header-flyout-link-list">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Foren</h4>
							<div class="inner">
								<h3 class="hidden-small">Übersicht</h3>
								<ul>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/41" class="link">Das neue FUSSBALL.DE<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/11" class="link">Alles zum Amateurfußball<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/21" class="link">Alles, nur kein Amateurfußball<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/31" class="link">Votings und Umfragen<span class="icon-link-arrow"></span></a>
									</li>
									<li>
										<a href="http://www.fussball.de/ugc/-/foren/91" class="link">Service<span class="icon-link-arrow"></span></a>
									</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="login" class="flyout-subnav">
			<div data-user-dependency="{'FBDE_USER_ID':'existVisible'}" class="container">
				<div class="flyout-left">
					<nav class="flyout-nav">
						<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Anmelden</h4>
						<ul>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-content"><span></span>Inhalte verwalten<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-account"><span></span>Kontoeinstellungen<span class="icon-angle-right"></span></div>
							</li>
							<li data-flyoutnavitem="sub" data-ng-class="{'current':isCurrent}">
								<div data-flyoutitem-identifier="#dashboard-profile"><span></span>Profil einrichten<span class="icon-angle-right"></span></div>
							</li>
						</ul>
					</nav>
				</div>
				<div class="flyout-right">
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-content" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Inhalte verwalten</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li>
											<a href="https://www.fussball.de/favorites" class="link">Deine Favoriten<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/images.and.videos.overview" class="link">Deine Bilder & Videos<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/account.photoalbum" class="link">Deine Fotoalben<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-mid">
											<a href="https://www.fussball.de/account.admin.widgets" class="link">Deine Widgets<span class="icon-link-arrow"></span></a>
										</li>
										<li class="hidden-small">
											<div data-user-dependency="{'FBDE_PROFILES':'inarraystartswith'}" data-user="{'FBDE_PROFILES':'TEAM'}">
												<a href="https://www.fussball.de/account.teams" class="link">Deine Mannschaftsseiten<span class="icon-link-arrow"></span></a>
											</div>
										</li>
										<li class="hidden-small">
											<a href="https://www.fussball.de/account.news" class="link">Deine Spielberichte & News<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url1150491" type="hidden" value="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/0201IGL94G000000VS54898DVUL01S6C/team-id/011MIDI43O000000VTVG0001VTR8C1K7">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-account" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Kontoeinstellungen</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li>
											<a href="https://www.fussball.de/account.admin" class="link">Benutzerprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a href="https://www.fussball.de/account.admin.player" class="link">Spielerprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a href="https://www.fussball.de/account.admin.referee" class="link">Schiriprofil verwalten<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url1150492" type="hidden" value="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/0201IGL94G000000VS54898DVUL01S6C/team-id/011MIDI43O000000VTVG0001VTR8C1K7">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div data-flyoutnavcontent="sub" data-ng-class="{'active':isActive}" id="dashboard-profile" class="flyout-tab">
						<div class="dashboard">
							<h4 data-ng-click="scopeEnv.isMainMenuHidden = true; scopeEnv.isSubMenuHidden = false;"><span class="icon-angle-left"></span>Profil einrichten</h4>
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Übersicht</h3>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'notinarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}" class="hidden-small">
											<a href="https://www.fussball.de/register.player?fw_url=http%3A%2F%2Fwww.fussball.de%2Fhomepage" class="link">Spielerprofil einrichten<span class="icon-link-arrow"></span></a>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'notinarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}" class="hidden-small">
											<a href="https://www.fussball.de/register.referee?fw_url=http%3A%2F%2Fwww.fussball.de%2Fhomepage" class="link">Schiriprofil einrichten<span class="icon-link-arrow"></span></a>
										</li>
									</ul>
								</div>
							</div>
						</div>
						<div class="profiles header-flyout-profiles">
							<div class="header-flyout-link-list">
								<div class="inner">
									<h3>Deine Profile auf FUSSBALL.DE</h3>
									<div class="logo-wrapper xinline_headerflyoutdashboardprofiles_1908">
										<div data-user-interpolate="innerHTML" data-user-interpolate-tmpl="Angemeldet als: %FBDE_NICKNAME%" class="meta xinline_headerflyoutdashboardprofiles_2011"></div>
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_dfbnet.png" alt="login" data-user="{'FBDE_PROVIDER':'2'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_fbde.png" alt="login" data-user="{'FBDE_PROVIDER':'1'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/FB-f-Logo__blue_58.png" alt="login" data-user="{'FBDE_PROVIDER':'3'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
										<img data-user-dependency="{'FBDE_PROVIDER':'equal'}" src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/provider_logo_google.png" alt="login" data-user="{'FBDE_PROVIDER':'4'}" class="logo xinline_headerflyoutdashboardprofiles_3786">
									</div>
									<ul>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'FAN'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%" class="link">Benutzer-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/fanprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/fanprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'SPIELER'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%" class="link">Spieler-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/spielerprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/spielerprofil.bearbeiten">Bearbeiten</a></span>
										</li>
										<li data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'REFEREE'}">
											<a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%" class="link">Schiedsrichter-Profil<span class="icon-link-arrow"></span></a>
											<span class="meta hidden-small"><a data-user-interpolate="href" data-user-interpolate-tmpl="http://www.fussball.de/schiedsrichterprofil/-/userid/%FBDE_USER_ID%">Ansehen</a> | <a href="https://www.fussball.de/schiedsrichterprofil.bearbeiten">Bearbeiten</a></span>
										</li>
									</ul>
									<div class="account-logout">
										<form method="POST" action="https://www.fussball.de/logout.fbde">
											<input name="fw_url" id="logout_fw_url1150493" type="hidden" value="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/0201IGL94G000000VS54898DVUL01S6C/team-id/011MIDI43O000000VTVG0001VTR8C1K7">
											<button type="submit" class="button button-primary button-block">Abmelden</button>
										</form>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div data-flyoutnavcontent="main" data-ng-class="{active:isActive, hidden: scopeEnv.isSubMenuHidden}" id="search" class="flyout-subnav">
			<div class="container displaystate">
				<h4 data-ng-click="scopeEnv.isMainMenuHidden = false; flyoutState.isOpen = false;"><span class="icon-angle-left"></span>Suche</h4>
				<div class="header-flyout-search">
					<form method="GET" action="//www.fussball.de/suche" data-rest-form>
						<div class="form-group form-dark">
							<div class="search-input">
								<div class="label-wrapper">
									<input data-ng-model="flyoutsearchQuery" name="text" placeholder="Suchbegriff eingeben*" id="flyout-search-query" type="text" value="">
									<label for="flyout-search-query"><span class="icon-search"></span></label>
								</div>
							</div>
							<div data-select-box="single" class="select-wrapper">
								<select size="1" name="restriction">
									<option value="-1">Gesamte Seite</option>
									<option value="CLUB_AND_TEAM">Vereine</option>
									<option value="PLAYER_PROFILE">Spielerprofile</option>
									<option value="FAN_PROFILE">Benutzerprofile</option>
									<option value="REFEREE_PROFILE">Schiedsrichterprofile</option>
									<option value="NEWS">News</option>
									<option value="UGC_NEWS">Mannschafts-News</option>
									<option value="PROFI_NEWS">Profi-Newsflash</option>
								</select>
							</div>
						</div>
						<div class="search-button">
							<button type="submit" class="button button-primary button-block">Finden</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</header><div data-ng-class="{active:flyoutState.isOpen, 'active-layer':layerState.isOpen, 'active-loader':loaderState.isActive}" data-ng-click="closeFlyout()" id="content-block"></div>

		

		<nav class="in-page-share">
	<ul>
		<li class="favorites">
			<ul>
				<li>
					<a href="https://www.fussball.de/add.favorite?fw_url=http%3A%2F%2Fwww.fussball.de%2Fmannschaft%2Ffc-astoria-walldorf-2-fc-astoria-walldorf-baden%2F-%2Fsaison%2F1718%2Fteam-id%2F011MIDI43O000000VTVG0001VTR8C1K7&object-ref=011MIDI43O000000VTVG0001VTR8C1K7&object-type=team&text=FC+Astoria+Walldorf+2+%28B-Junioren%29"><span class="icon-favorits"></span></a>
				</li>
			</ul>
		</li>
		<li class="facebook sharing">
			<a href="" data-share-page="facebook" target="_blank"><span class="icon-facebook"></span></a>
		</li>
		<li class="twitter sharing">
			<a href="" data-share-page="twitter" target="_blank"><span class="icon-twitter"></span></a>
		</li>
		<li class="googleplus sharing">
			<a href="" data-share-page="googleplus" target="_blank"><span class="icon-googleplus"></span></a>
		</li>
	</ul>
</nav>

		<div class="content" data-ng-class="{flyoutopened:flyoutState.isOpen}" >
			

		<section id="stage" class="profile-theme-blue" data-lazyload>
	<div class="stage-team stage-profile">
		<div class="background-image"></div>
		<div class="stage-profile-content container">
			<p class="subline">B-Junioren
				<span class="separator">&#124;</span>
				<a href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180">Baden</a>
			</p>
			<h2>FC Astoria Walldorf 2</h2>
			<p class="subline">
				<a href="http://www.fussball.de/verein/fc-astoria-walldorf-baden/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I">Zur Vereinsseite</a>
			</p>
			<div class="stage-content-wrapper">
				<div class="column-left">
					<div class="column-image">
						<div class="img">
							<img src="//service.media.fussball.de/api/uimg/cont/-/ID/011MIDI43O000000VTVG0001VTR8C1K7/TYP/50/SZ/3" alt="image">
							<div class="hexagon club">
								<span class="icon-hexagon"></span>
								<div class="inner">
									<div class="valign-wrapper">
										<div class="valign-inner">
											<img src="//www.fussball.de/export.media/-/action/getLogo/format/0/id/00ES8GN9B8000083VV0AG08LVUPGND5I" alt="logo">
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="column-right">
					<div class="inner">
						<a href="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G" class="profile-value">bfv-B-Junioren Landesliga Rhein/Neckar</a>
						<p class="profile-label">Wettbewerb</p>
						<p class="profile-value">1</p>
						<p class="profile-label">Tabellenplatz</p>
						<p class="profile-value">42</p>
						<p class="profile-label">Punkte</p>
						<p class="profile-value">105:9</p>
						<p class="profile-label">Torverhältnis</p>
						<p class="profile-value">Landesliga</p>
						<p class="profile-label">Spielklasse</p>
						<div class="profile-edit">
							<div data-user-dependency="{'FBDE_PROFILES':'inarraystartswith'}" data-user="{'FBDE_PROFILES':'TEAM'}">
								<a data-user-dependency="{'FBDE_TEAMS':'inarray'}" data-user="{'FBDE_TEAMS':'011MIDI43O000000VTVG0001VTR8C1K7'}" href="https://www.fussball.de/mannschaft.bearbeiten/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7"><span class="icon-edit"></span><span class="text-edit">Mannschaftsseite bearbeiten</span></a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>



<section id="team-quickview" class="profile-theme-blue" data-lazyload>
	<div data-settings="{ 'showamount':{'mobile':1, 'tablet':1, 'desktop':2}, 'removestyle':true, 'positioning':{'1':['50%']} }" class="team-quick-view cycle-slider">
		<div class="container">
			<ul>
				<li data-ng-style="styled" data-ng-class="{'active':visible}" data-cycle-slider-element>
					<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-dossenheim-ziegelh-peterstal-1/-/spiel/020GBC217K000000VS54898EVVII0TR2">
						<div class="match-wrapper">
							<div class="match-meta"><span>Letztes Spiel: Sa, 07.04.2018</span><span class="separator"> &#124; </span><span>11:00 &#124; Meisterschaften</span></div>
							<div class="match-teams"><span class="team-home">SG Dossenheim/&#8203;Ziegelhausen-Peterstal</span><span class="colon"> - </span><span class="team-away">FC Astoria Walldorf 2</span></div>
							<div class="match-score"><span data-obfuscation="d5of81qa" class="score-left">&#xE67B;</span><span class="colon">:</span><span data-obfuscation="d5of81qa" class="score-right">&#xE6A3;&#xE6B0;<span class="icon-verified"></span></span></div>
						</div>
					</a>
				</li>
				<li data-ng-style="styled" data-ng-class="{'active':visible}" data-cycle-slider-element>
					<a href="http://www.fussball.de/spiel/tsg-91-09-luetzelsachsen-fc-astoria-walldorf-2/-/spiel/020GBC1TNC000000VS54898EVVII0TR2">
						<div class="match-wrapper">
							<div class="match-meta"><span>Nächstes Spiel: Sa, 14.04.2018</span><span class="separator"> &#124; </span><span>11:00 &#124; Meisterschaften</span></div>
							<div class="match-teams"><span class="team-home">FC Astoria Walldorf 2</span><span class="colon"> - </span><span class="team-away">TSG 91/&#8203;09 Lützelsachsen</span></div>
							<div class="match-score"><span data-obfuscation="d5of81qa" class="score-left">&#xE66E;</span><span class="colon">:</span><span data-obfuscation="d5of81qa" class="score-right">&#xE6B2;</span></div>
						</div>
					</a>
				</li>
			</ul>
		</div>
		<div class="previous">
			<a rel="prev" data-ng-click="prev()" href="javascript://"><span class="icon-angle-ultralight-left"></span></a>
		</div>
		<div class="next">
			<a rel="next" data-ng-click="next()" href="javascript://"><span class="icon-angle-ultralight-right"></span></a>
		</div>
	</div>
</section>
<section id="teamNews">
	<div class="ticker-container">
		<h2><span>Mannschafts-News</span></h2>
		<div class="info">
			<p>Für den FC Astoria Walldorf 2 wurden noch keine Mannschafts-News angelegt.</p>
			<div class="profile-edit hidden-small">
				<div data-user-dependency="{'FBDE_PROFILES':'inarraystartswith'}" data-user="{'FBDE_PROFILES':'TEAM'}">
					<a data-user-dependency="{'FBDE_TEAMS':'inarray'}" data-user="{'FBDE_TEAMS':'011MIDI43O000000VTVG0001VTR8C1K7'}" href="https://www.fussball.de/mannschaft.news.bearbeiten/-/object-ref/011MIDI43O000000VTVG0001VTR8C1K7/team-id/011MIDI43O000000VTVG0001VTR8C1K7"><span class="button-small button button-primary">Mannschafts-News anlegen</span></a>
				</div>
			</div>
		</div>
	</div>
</section>

<section id="mediastream">
    <div class="wrapper" data-mediastream="http://service.media.fussball.de/api/mediastream/ajax/-/team/011MIDI43O000000VTVG0001VTR8C1K7"
         data-mediastream-id="xxxxxx"
         data-streamitemmeta="http://service.media.fussball.de/api/global/ajax_view.html"
         data-offsetleft='{"desktop":0, "tablet":0, "mobile":0}'
         data-user-dependency="{'FBDE_USER_ID':'exist'}"
         data-tv-video-quality-selector-binding="quality" > <!-- [patch:3746] component:quality -->

        <div class="loader" data-ng-class="{loaded:initalized}" data-lazyload></div>

        <div class="stream">
            <div class="info-box counter">
                <span class="primary" data-ng-bind="streamitem.maxIndex">0</span>
                <div class="secondary">Bilder / Videos</div>
            </div>

            <div class="background-wrapper">
                <ul data-itemwidth="180">
                    <li data-ng-repeat="item in streamItems | orderBy:'item.id'" data-mediastreamitem="{{item.id}}" data-ng-class="{active:active, infront:infront, adjusting:adjusting, video:item.type=='video'}">
                        <a data-ng-click="openBigView()">
                            <img data-ng-src="{{item.thumb}}" data-imageload/>
                        </a>
                    </li>

                    <li class="no-uploads" data-mediastreamitemfallback>
                        <span>Zeig&#x27;s uns! Lade dein Video oder Foto hoch!</span>
                    </li>
                </ul>
            </div>

            <div class="info-box upload" data-ng-click="showUpload()">
                <span class="primary">+</span>
                <div class="secondary">Jetzt Hochladen</div>
            </div>
        </div>

        <div class="sub-view" data-ng-class="{show:subView.open, item: subView.current == 'item', upload: subView.current == 'upload'}">
            <div class="sub-view-wrapper">

                <span data-ng-click="closeSubView()" class="icon-close"></span>

                <div class="item-view" data-ng-class="{show:subView.current == 'item'}">
                    <div class="bigimage">
                        <div class="control-wrapper">

                            <p class="itemindex">{{streamitem.content.streamDataIndex+1}} / {{streamitem.maxIndex}}</p>

                            <div class="bigimage-image" data-ng-class="{show:streamitem.content.type == 'image'}">
                                <img data-ng-src="{{streamitem.image}}" alt="galerie" data-imageload='{"setSize":true}'>
                            </div>

                            <div class="bigimage-video" data-ng-class="{show:streamitem.content.type == 'video'}">
								<!-- components::video_player -->
<div class="video-player"  data-video data-swf="//www.fussball.de/static/por/6.80.99.3077/swf/videoplayer.swf">
	<video autobuffer controls data-ng-hide="video.flashFallback()">

	</video>

	<div class="flash-fallback" data-ng-show="video.flashFallback()">

	</div>

	<a href="" class="flashPlayPause" data-ng-show="video.flashFallback()" data-ng-click="playPause()"></a>

</div>
<!-- /components::video_player -->

							</div>

                            <div class="previous" data-ng-class="{available:streamitem.enablePrev}">
								              <a href="javascript://" rel="prev" data-ng-click="prevStreamitem()">
                                	<span class="icon-angle-ultralight-left"></span>
                           		</a>
                            </div>
                            <div class="next" data-ng-class="{available:streamitem.enableNext}">
                            	<a href="javascript://" rel="next" data-ng-click="nextStreamitem()">
                                	<span class="icon-angle-ultralight-right"></span>
                                </a>
                            </div>

                            <!-- snippet::video_quality_horizontal -->
<!-- .hide-qualities - die Klasse wird zur Steuerung der Sichtbarkeit in Media-Stream verwendet! -->
<div class="form-kit" ng-class="{ 'hide-qualities' : !showQualities }" >
  <div class="form-element quality-form-element"
       data-ng-controller="TvVideoQualityController"
       data-radio-group="quality">

      <label class="main quality-level quality-title" >Qualität</label>
      <div class="quality-level quality-entry"
           data-ng-repeat="qualityItem in qualities" >
          <label class="radio small" >
              <span class="radio-button"></span>
              <input type="radio"
                     name="quality"
                     value="{{ qualityItem.value }}" />
              <span class="label">{{ qualityItem.title }}</span>
          </label>
      </div>

  </div>
</div>
<!-- /snippet::video_quality_horizontal -->


                            <div class="mediastream-content">
                                <span class="meta" data-ng-if="streamitem.content.user">
									Hochgeladen am {{streamitem.content.date}} um {{streamitem.content.time}} Uhr von <a data-ng-href="{{streamitem.content.userurl}}">{{streamitem.content.user}}<span class="icon-link-arrow"></span></a>
								</span>
								<span class="meta" data-ng-if="!streamitem.content.user">
									Hochgeladen am {{streamitem.content.date}} um {{streamitem.content.time}} Uhr
								</span>
                                <h3>{{streamitem.content.title}}</h3>
                                <p>
                                    {{streamitem.content.description}}
                                </p>
                                <div class="detailed-informations" data-ng-show="streamitem.content.loaded">
                                    <div class="numberOfViews">
                                        <span data-ng-bind="streamitem.content.views">0</span>
                                        <span class="text" data-ng-pluralize count="streamitem.content.views" when="{'1': 'Aufruf', 'other': 'Aufrufe'}"></span>
                                    </div>
                                    <div class="seperator">|</div>
                                    <div class="number-of-comments">
                                        <span data-ng-bind="streamitem.content.comments">0</span>
                                        <span class="text" data-ng-pluralize count="streamitem.content.comments" when="{'1': 'Kommentar', 'other': 'Kommentare'}"></span>
                                    </div>
                                    <div class="seperator">|</div>
                                    <div class="rating">
                                        <div class="stars">
                                            <span class="star" data-ng-class="{active:getStarRating(1)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(2)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(3)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(4)}"></span>
                                            <span class="star" data-ng-class="{active:getStarRating(5)}"></span>
                                        </div>
                                        <span data-ng-bind="streamitem.content.ratings">0</span>
                                        <span data-ng-pluralize count="streamitem.content.ratings" when="{'1': 'Bewertung', 'other': 'Bewertungen'}"></span>
                                    </div>
                                </div>
                                <a data-ng-href="{{streamitem.content.targetName}}" class="commentAndShare">Kommentieren, bewerten und melden<span class="icon-link-arrow"></span></a>
                            </div>
                        </div>
                    </div>
				</div>
                <div class="upload-view upload-component" data-ng-class="{show:subView.current == 'upload'}" data-fileupload="http://service.media.fussball.de/api/upload/ajax"  data-fileupload-check="true" data-postdef='{"key1":"value1", "key2":"value2", "key3":"value3"}'>
                        <!-- components::upload -->
<form id="fileupload" action="#" method="POST" enctype="multipart/form-data">
    <div class="header-intro">
        <div class="before-upload">
            <h3 class="headline">
                Zeig’s uns! Lade deine Bilder und Videos hoch!
            </h3>

            <p class="upload-informations">
                Mögliche Bildformate sind JPG, PNG und GIF. Die Dateigröße sollte 2 MB nicht überschreiten. Wir unterstützen folgende Videoformate MPG, MP4, AVI, MOV und WMV. Dein Video sollte nicht größer als 100 MB sein.
				<br>
				Bitte beachte nach dem Veröffentlichen Deiner Bilder und Videos, dass die Konvertierung der Dateien etwas Zeit beansprucht, sodass Du die Bilder bzw. Videos nicht sofort siehst. Habe bitte etwas Geduld.
            </p>

            <div class="form-kit">
                <div class="form-element buttons step">
                    <span class="button button-primary add-files" data-ng-class="{disabled: disabled}">
                        <span class="text"><span>+</span>Dateien hinzufügen</span>
                        <input data-ng-file-select type="file" multiple>
                    </span>
                    <button class="button button-primary" type="button" data-ng-click="uploader.uploadAll()" data-ng-disabled="!uploader.getNotUploadedItems().length">
                        Upload starten
                    </button>
                    <button class="button button-primary" type="button" data-ng-click="releaseAllFiles(uploader.queue)" data-ng-show="allFilesUploaded(uploader.queue)" data-ng-disabled="!allFilesReadyTorelease(uploader.queue)">
                        Alle Veroeffentlichen
                    </button>
                </div>
            </div>
        </div>
    </div>
</form>

<div class="files">
    <ul>
        <li data-ng-repeat="item in uploader.queue" data-meta data-url-release="https://service.media.fussball.de/api/upload/release/-/team/011MIDI43O000000VTVG0001VTR8C1K7" data-url-update="https://service.media.fussball.de/api/upload/update/-/team/011MIDI43O000000VTVG0001VTR8C1K7" data-url-delete="https://service.media.fussball.de/api/upload/delete">

            <div class="item-wrapper">
                <div class="file-thumbnail-wrapper">
                    <div class="file-thumbnail">
                        <div data-ng-show="uploader.isHTML5 && controller.filetype(item.file) == 'image'" data-thumb="{ file: item.file, height: 70 }"></div>
                        <img data-ng-show="!uploader.isHTML5 && controller.filetype(item.file) == 'image'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_image.png" alt="">
                        <img data-ng-show="controller.filetype(item.file) == 'video'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_video.png" alt="">
                        <img data-ng-show="controller.filetype(item.file) == 'default'" src="//www.fussball.de/static/por/6.80.99.3077/images/fileupload/type_default.png" alt="">
                    </div>
                </div>

                <div class="file-meta" data-ng-class="{'video':item.isUploaded && item.isSuccess && controller.filetype(item.file) == 'video'}">
                    <span class="file-name">
                        {{item.file.name}}
                    </span>
                    <span class="file-size" data-ng-show="uploader.isHTML5">
                        {{ item.file.size/1024/1024|number:2 }} Mb
                    </span>
                    <span class="file-error" data-ng-show="item.error.show">
                        {{item.error.plainText ? item.error.message : (item.error.message | translate)}}
                    </span>
                    <div class="span file-convert" data-ng-show="item.isUploaded && item.isSuccess && controller.filetype(item.file) == 'video'">
                        Dein hochgeladenes Video wird noch konvertiert, was einige Zeit dauern kann. Du kannst dein Video später unter &quot;Meine Bilder und Videos&quot; freigeben und eine Beschreibung hinzufügen.
                    </div>
                </div>

                <div class="file-progress" data-ng-show="item.isUploading && uploader.isHTML5">
                    <div class="file-progressbar" data-ng-style="{ 'width': item.progress + '%' }"></div>
                </div>

                <div class="file-action">
                    <div class="form-kit">
                        <div class="form-element buttons step">
                            <button class="button file-button-cancel" type="button" data-ng-click="item.cancel()" data-ng-show="item.isUploading">
                                <span class="icon-close"></span>
                                Abbrechen
                            </button>
                            <button class="button file-button-delete" type="button" data-ng-click="item.remove()" data-ng-show="!item.isUploading && !item.isSuccess">

                                Löschen
                            </button>
                            <button class="button file-button-edit" type="button" data-ng-click="item.tab = !item.tab"  data-ng-show="item.isUploaded && item.isSuccess">
                                <span class="icon-edit"></span>
                                Bearbeiten
                            </button>
                            <button class="button button-primary file-button-release" data-ng-click="releaseItem(item)" type="button" data-ng-show="item.isUploaded && item.isSuccess" data-ng-disabled="!checkMetaTitle()">
                                Veröffentlichen
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="tab" data-ng-show="item.tab">
                <form ng-submit>
                    <div class="form-element text">
                        <label class="main">Titel
                            <input type="text" data-ng-model="metaTitle" name="title" maxlength="100">
                            <p data-remainingchars="nomodel" data-ng-cloak class="ng-cloak">{{remainingchars}} Zeichen möglich</p>
                        </label>
                    </div>

                    <div class="form-element textarea">
                        <label class="main">Beschreibung
                            <textarea name="message" data-ng-model="metaMessage" maxlength="1000" cols="30" rows="10"></textarea>
                            <p data-remainingchars="nomodel" data-ng-cloak class="ng-cloak">{{remainingchars}} Zeichen möglich</p>
                        </label>
                    </div>

                    <div class="form-element buttons step">
                        <a href="javascript://" data-ng-click="abortEdit()">Abbrechen<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="updateItem(item)">Speichern<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="deleteItem(item)">Löschen<span class="icon-link-arrow"></span></a>
                        <a href="javascript://" data-ng-click="overwriteSiblings(item)">Titel/Text für alle Dateien übernehmen<span class="icon-link-arrow"></span></a>
                    </div>
                </form>
            </div>

        </li>
    </ul>
</div>
<!-- /components::upload -->

                </div>
            </div>
        </div>
    </div>
</section>


<section class="wm-section">
	<div data-wm-type="super" class="wm-container">
		<div class="wm-container-inner">
			<div data-ad-sizes="[[320,50], [468,60], [728,90]]" data-ad-local-link="http://www.fussball.de/newsdetail/push-ticker-und-mehr-das-bietet-unsere-app/-/article-id/127931#!/section/stage" data-ad-breakpoints="phone,tablet,desktop" data-ad-local-image="{'desktop': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-sb.png', 'tablet': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-fsb.png', 'phone':'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-mb.png'}" class="wm-iframe" data-ad-local-link-target="_top">
				<p>Anzeige</p>
				<div id="slot-2895462">
					<script type="text/javascript">wmConfig.registerRenderSlot('slot-2895462');</script>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="team-squad" class="profile-theme-blue" data-lazyload>
	<div id="team-squad-wrapper">
		<div class="team_squad_tab_group">
			<div data-toggle="li a" data-ng-controller="AjaxController" data-type="ajax" class="tab-group" data-tab-group>
				<ul>
					<li class="on">
						<a data-tracking-name="mannschaft_kader/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_kader" data-ajax-target="#team-squad-wrapper" data-ajax-resource="http://www.fussball.de/ajax.team.squad/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.squad/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.squad/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Kader</a>
					</li>
					<li>
						<a data-tracking-name="mannschaft_neuzugaenge/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_neuzugaenge" data-ajax-target="#team-squad-wrapper" data-ajax-resource="http://www.fussball.de/ajax.team.squad.arrivals/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.squad.arrivals/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.squad.arrivals/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Neuzugänge</a>
					</li>
					<li>
						<a data-tracking-name="mannschaft_abgaenge/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_abgaenge" data-ajax-target="#team-squad-wrapper" data-ajax-resource="http://www.fussball.de/ajax.team.squad.departures/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.squad.departures/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.squad.departures/-/order-by/1/saison/1718/show-filter/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Abgänge</a>
					</li>
				</ul>
			</div>
		</div>
		<div>
			<div class="team-squad-table">
				<div data-toggle=".filter-toggle" data-ng-controller="AjaxController" class="team-squad-filter-nav table-filter">
					<div class="filter-toggle">Filter<span class="icon-close"></span></div>
					<div class="filter-content">
						<div class="row">
							<form data-ajax-type="html" data-ajax-target="#team-squad-wrapper" data-ajax-defaults="{'saison':'17/18', 'order-by': '1'}" data-ajax-resource="http://www.fussball.de/ajax.team.squad/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-ajax="replace" data-ajax-method="post" data-tracking="{'href':'http://www.fussball.de/ajax.team.squad/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}">
								<div data-select-box="single" data-select-box-default="0" data-select-title="Saison" class="select-wrapper" data-ajaxmodel="saison">
									<select size="1" name="saison">
										<option value="1718" class="selected" selected="selected">2017/2018</option>
										<option value="1617">2016/2017</option>
										<option value="1516">2015/2016</option>
										<option value="1415">2014/2015</option>
										<option value="1314">2013/2014</option>
										<option value="1213">2012/2013</option>
										<option value="1112">2011/2012</option>
										<option value="1011">2010/2011</option>
										<option value="0910">2009/2010</option>
										<option value="0809">2008/2009</option>
										<option value="0708">2007/2008</option>
										<option value="0607">2006/2007</option>
										<option value="0506">2005/2006</option>
										<option value="0405">2004/2005</option>
									</select>
								</div>
								<div data-select-box="single" data-select-box-default="0" data-select-title="Sortiert nach" class="select-wrapper" data-ajaxmodel="order-by">
									<select size="1" name="order-by">
										<option value="1" class="selected" selected="selected">Einsätze</option>
										<option value="2">Spieler</option>
										<option value="5">Einsatzminuten</option>
										<option value="6">Tore</option>
									</select>
								</div>
								<button type="submit" class="button button-primary">Los</button>
							</form>
						</div>
					</div>
					<div class="filter-message">
						<div class="row">
							<p class="headline">Die Kaderliste ist bisher nicht zur Veröffentlichung freigegeben.</p>
							<span data-user-dependency="{'FBDE_PROFILES':'inarray'}" data-user="{'FBDE_PROFILES':'TEAMADMIN'}"><a data-user-dependency="{'FBDE_SA_TEAMS':'inarray'}" data-user="{'FBDE_SA_TEAMS':'011MIDI43O000000VTVG0001VTR8C1K7'}" href="https://www.fussball.de/mannschaft.bearbeiten/-/action/SQUAD_PUBLISH_OPEN/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="button button-primary button-small"><span>Kader veröffentlichen</span></a></span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="id-team-matchplan">
	<div data-toggle="li a" data-ng-controller="AjaxController" data-type="ajax" class="tab-group" data-tab-group>
		<ul>
			<li class="on">
				<a data-tracking-name="mannschaft_naechstespiele/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_naechstespiele" data-ajax-target="#id-team-matchplan-table" data-ajax-resource="http://www.fussball.de/ajax.team.next.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.next.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.next.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Nächste Spiele</a>
			</li>
			<li>
				<a data-tracking-name="mannschaft_letztespiele/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_letztespiele" data-ajax-target="#id-team-matchplan-table" data-ajax-resource="http://www.fussball.de/ajax.team.prev.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.prev.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.prev.games/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Letzte Spiele</a>
			</li>
			<li>
				<a data-tracking-name="mannschaft_spielplan/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_spielplan" data-ajax-target="#id-team-matchplan-table" data-ajax-resource="//www.fussball.de/ajax.team.matchplan/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="//www.fussball.de/ajax.team.matchplan/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'//www.fussball.de/ajax.team.matchplan/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Mannschaftsspielplan</a>
			</li>
		</ul>
	</div>
	<div id="id-team-matchplan-table" class="table-container fixtures-matches-table club-matchplan-table">
		<table class="table table-striped table-full-width">
			<thead>
				<tr class="thead hidden-small">
					<th class="hidden-small">Datum | Zeit</th>
					<th colspan="3">Wettbewerb</th>
					<th colspan="2"><span class="hidden-small">Info</span></th>
				</tr>
			</thead>
			<tbody>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 14.04.2018 - 11:00 Uhr | Landesliga</td>
				</tr>
				<tr class="odd row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 14.04.18 |&nbsp;</span>11:00</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115092</a>
					</td>
				</tr>
				<tr class="odd">
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/tsg-91-09-luetzelsachsen-tsg-91-09-luetzelsachsen-baden/-/saison/1718/team-id/011MIC2U1G000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="TSG 91/09 Lützelsachsen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800009QVV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								TSG 91/&#8203;09 Lützelsachsen
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/tsg-91-09-luetzelsachsen-fc-astoria-walldorf-2/-/spiel/020GBC1TNC000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE670;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE69D;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/tsg-91-09-luetzelsachsen-fc-astoria-walldorf-2/-/spiel/020GBC1TNC000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Mittwoch, 18.04.2018 - 19:00 Uhr | Verbands-Pokal</td>
				</tr>
				<tr class="row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Mi, 18.04.18 |&nbsp;</span>19:00</td>
					<td colspan="3" class="column-team">
						<a>Verbands-Pokal</a>
					</td>
					<td colspan="2">
						<a>PO | 921035015</a>
					</td>
				</tr>
				<tr>
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/fc-noettingen-fc-noettingen-baden/-/saison/1718/team-id/011MIAJ3OG000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Nöttingen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9CG000062VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Nöttingen
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/fc-noettingen-fc-astoria-walldorf-2/-/spiel/022VQ5JIHK000000VS54898EVV9D0TPO"><span data-obfuscation="cqcyow1o" class="score-left">&#xE6BC;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE67F;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/fc-noettingen-fc-astoria-walldorf-2/-/spiel/022VQ5JIHK000000VS54898EVV9D0TPO"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 21.04.2018 - 16:00 Uhr | Landesliga</td>
				</tr>
				<tr class="odd row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 21.04.18 |&nbsp;</span>16:00</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115102</a>
					</td>
				</tr>
				<tr class="odd">
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/tsg-62-09-weinheim-tsg-62-09-weinheim-baden/-/saison/1718/team-id/011MICLQ1K000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="TSG 62/09 Weinheim" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A8VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								TSG 62/&#8203;09 Weinheim
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-tsg-62-09-weinheim/-/spiel/020GBC1T10000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE67F;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE67F;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-tsg-62-09-weinheim/-/spiel/020GBC1T10000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 28.04.2018 - 15:45 Uhr | Landesliga</td>
				</tr>
				<tr class="row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 28.04.18 |&nbsp;</span>15:45</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115107</a>
					</td>
				</tr>
				<tr>
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/vfl-kurpfalz-mannheim-neckarau-vfl-kurpfalz-mannheim-neckarau-baden/-/saison/1718/team-id/01E03IV450000000VV0AG811VTA8FO8N" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="VfL Kurpfalz Mannheim-Neckarau" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008RVV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								VfL Kurpfalz Mannheim-Neckarau
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/vfl-kurpfalz-mannheim-neckarau-fc-astoria-walldorf-2/-/spiel/020GBC1QP0000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE6BA;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE69D;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/vfl-kurpfalz-mannheim-neckarau-fc-astoria-walldorf-2/-/spiel/020GBC1QP0000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Donnerstag, 10.05.2018 - 11:00 Uhr | Kreispokal</td>
				</tr>
				<tr class="odd row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Do, 10.05.18 |&nbsp;</span>11:00</td>
					<td colspan="3" class="column-team">
						<a>Kreispokal</a>
					</td>
					<td colspan="2">
						<a>PO | 920694030</a>
					</td>
				</tr>
				<tr class="odd">
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/sg-eppelheim-pfaffengrund-asv-eppelheim-baden/-/saison/1718/team-id/016J4O7ANO000000VV0AG811VSBH97M6" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="SG Eppelheim/Pfaffengrund" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006QVV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								SG Eppelheim/&#8203;Pfaffengrund
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-eppelheim-pfaffengrund/-/spiel/020JV79RTC000000VS54898EVV27PHDA"><span data-obfuscation="cqcyow1o" class="score-left">&#xE684;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE69D;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-eppelheim-pfaffengrund/-/spiel/020JV79RTC000000VS54898EVV27PHDA"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 12.05.2018 - 15:45 Uhr | Landesliga</td>
				</tr>
				<tr class="row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 12.05.18 |&nbsp;</span>15:45</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115117</a>
					</td>
				</tr>
				<tr>
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/vfb-eppingen-2-vfb-eppingen-baden/-/saison/1718/team-id/01A4655LQ4000000VV0AG811VSUI9EOJ" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="VfB Eppingen 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800004VVV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								VfB Eppingen 2
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/vfb-eppingen-2-fc-astoria-walldorf-2/-/spiel/020GBC1MFK000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE670;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE67A;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/vfb-eppingen-2-fc-astoria-walldorf-2/-/spiel/020GBC1MFK000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 02.06.2018 - 15:45 Uhr | Landesliga</td>
				</tr>
				<tr class="odd row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 02.06.18 |&nbsp;</span>15:45</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115126</a>
					</td>
				</tr>
				<tr class="odd">
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/sg-waibstadt-meckesheim-moenchzell-daisbach-sg-waibstadt-baden/-/saison/1718/team-id/01SMKMQ6C8000000VS548985VU8O1RK1" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="SG Waibstadt/Meckesheim-Mönchzell/Daisbach" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800005SVV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								SG Waibstadt/&#8203;Meckesheim-Mönchzell/&#8203;Daisbach
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-waibstadt-meckesheim-moenchzell-daisbach/-/spiel/020GBC1LLG000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE684;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE68F;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-waibstadt-meckesheim-moenchzell-daisbach/-/spiel/020GBC1LLG000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
				<tr class="row-headline visible-small">
					<td colspan="6">Samstag, 09.06.2018 - 15:15 Uhr | Landesliga</td>
				</tr>
				<tr class="row-competition hidden-small">
					<td class="column-date"><span class="hidden-small inline">Sa, 09.06.18 |&nbsp;</span>15:15</td>
					<td colspan="3" class="column-team">
						<a>Landesliga</a>
					</td>
					<td colspan="2">
						<a>ME | 320115127</a>
					</td>
				</tr>
				<tr>
					<td class="hidden-small"></td>
					<td class="column-club">
						<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Astoria Walldorf 2
							</div>
						</a>
					</td>
					<td class="column-colon">:</td>
					<td class="column-club no-border">
						<a href="http://www.fussball.de/mannschaft/fc-zuzenhausen-fc-zuzenhausen-baden/-/saison/1718/team-id/01E0PF8DBG000000VV0AG80NVV2L7DJE" class="club-wrapper">
							<div class="club-logo table-image"><span data-alt="FC Zuzenhausen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000060VV0AG08LVUPGND5I"></span></div>
							<div class="club-name">
								FC Zuzenhausen
							</div>
						</a>
					</td>
					<td class="column-score">
						<a href="http://www.fussball.de/spiel/fc-zuzenhausen-fc-astoria-walldorf-2/-/spiel/020GBC1IKO000000VS54898EVVII0TR2"><span data-obfuscation="cqcyow1o" class="score-left">&#xE670;</span><span class="colon">:</span><span data-obfuscation="cqcyow1o" class="score-right">&#xE69A;</span></a>
					</td>
					<td class="column-detail">
						<a href="http://www.fussball.de/spiel/fc-zuzenhausen-fc-astoria-walldorf-2/-/spiel/020GBC1IKO000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
					</td>
				</tr>
			</tbody>
		</table>
		<div data-toggle=".legend > span, .note > span" class="table-meta">
			<ul class="functions">
				<li class="legend"><span data-toggle-content=".table-legend">Legende<span class="icon-angle-down"></span></span></li>
				<li class="print">
					<a href="javascript: window.print();">Drucken<span class="icon-link-arrow"></span></a>
				</li>
			</ul>
			<div class="table-legend">
				<h3>Kürzel bei einem Spiel</h3>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>u</span></div>
							<div class="description">(U) Sportgerichtsurteil (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Annuliert</span></div>
							<div class="description">Annullierung</div>
						</div>
						<div class="column">
							<div class="item"><span>v</span></div>
							<div class="description">(V) Verwaltungsentscheid (bestätigt)</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>Absetzung</span></div>
							<div class="description">Spielabsetzung</div>
						</div>
						<div class="column">
							<div class="item"><span>w</span></div>
							<div class="description">(W) Wertung Spielinstanz (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Ausfall</span></div>
							<div class="description">Spielausfall</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>t</span></div>
							<div class="description">(T) Testspiel (bestätigt)</div>
						</div>
						<div class="column">
							<div class="item"><span>Abbruch</span></div>
							<div class="description">Spielabbruch</div>
						</div>
						<div class="column">
							<div class="item"><span>zg.</span></div>
							<div class="description">Diese Mannschaft wurde zurückgezogen, die Ergebnisse werden aber eingerechnet.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>Nichtantritt BEIDE</span></div>
							<div class="description">nicht angetretene Mannschaften</div>
						</div>
						<div class="column">
							<div class="item"><span>Nichtantritt HEIM</span></div>
							<div class="description">nicht angetreten HEIM-Mannschaft</div>
						</div>
						<div class="column">
							<div class="item"><span>Nichtantritt GAST</span></div>
							<div class="description">nicht angetreten GAST-Mannschaft</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>nV</span></div>
							<div class="description">nach Verlängerung</div>
						</div>
						<div class="column">
							<div class="item"><span>nE</span></div>
							<div class="description">nach Elfmeterschießen</div>
						</div>
					</div>
				</div>
				<h3>Sonstiges</h3>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span>**</span></div>
							<div class="description">Die Anstoßzeit steht noch nicht fest oder ist nicht bekannt.</div>
						</div>
						<div class="column">
							<div class="item"><span>o.E.</span></div>
							<div class="description">Keine Ergebnisanzeige, da die Staffel nicht im Leistungsbetrieb spielt.</div>
						</div>
						<div class="column">
							<div class="item"><span>oW</span></div>
							<div class="description">Mannschaften mit diesem Kennzeichen spielen außer Konkurrenz.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span class="icon-verified"></span></div>
							<div class="description">Ergebnis bestätigt</div>
						</div>
						<div class="column">
							<div class="item"><span>Live</span></div>
							<div class="description">Liveticker</div>
						</div>
						<div class="column">
							<div class="item"><span>SPIELFREI</span></div>
							<div class="description">An diesem Datum hat die Mannschaft spielfrei.</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="wrapper">
						<div class="column">
							<div class="item"><span class="icon-article"></span></div>
							<div class="description">Spielbericht vorhanden</div>
						</div>
						<div class="column">
							<div class="item"><span class="icon-foto"></span></div>
							<div class="description">Foto oder Video vorhanden</div>
						</div>
						<div class="column">
							<div class="item"><span class="icon-video"></span></div>
							<div class="description">Livestream oder Highlights vorhanden</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section><div data-wm-type="super" class="wm-container">
	<div class="wm-container-inner">
		<div data-ad-sizes="[[320,50], [468,60], [728,90]]" data-ad-local-link="http://www.fussball.de/newsdetail/push-ticker-und-mehr-das-bietet-unsere-app/-/article-id/127931#!/section/stage" data-ad-breakpoints="phone,tablet,desktop" data-ad-local-image="{'desktop': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-sb.png', 'tablet': 'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-fsb.png', 'phone':'http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/components/banner/placeholder-mb.png'}" class="wm-iframe" data-ad-local-link-target="_top">
			<p>Anzeige</p>
			<div id="slot-2895476">
				<script type="text/javascript">wmConfig.registerRenderSlot('slot-2895476');</script>
			</div>
		</div>
	</div>
</div>
<section id="team-competitions" class="profile-theme-blue" data-lazyload>
	<div class="team-competitions">
		<div class="factfile factfile-dark">
			<div class="factfile-headline">
				<h3 class="headline">Aktuelle Wettbewerbe</h3>
			</div>
			<div class="factfile-data">
				<div class="row">
					<div class="column-left">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-landesliga-rhein-neckar-baden-b-junioren-landesliga-b-junioren-saison1718-baden/-/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G">bfv-B-Junioren Landesliga Rhein/Neckar</a>
						</div>
						<div class="label">Meisterschaft</div>
					</div>
					<div class="column-right">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/bfv-b-junioren-kreispokal-kreis-heidelberg-kreis-heidelberg-b-junioren-kreispokal-b-junioren-saison1718-baden/-/staffel/020GMOE6TS000000VS54898EVVII0TR2-C">BFV-B-Junioren-Kreispokal, Kreis Heidelberg</a>
						</div>
						<div class="label">Pokal</div>
					</div>
				</div>
				<div class="row">
					<div class="column-left">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/bfv-verbandspokal-der-b-junioren-2017-18-baden-b-junioren-verbandspokal-b-junioren-saison1718-baden/-/staffel/022HUIK7SK000000VS54898DVSFFDR7Q-C">bfv-Verbandspokal der B-Junioren 2017-18</a>
						</div>
						<div class="label">Pokal</div>
					</div>
					<div class="column-right">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/fs-bj-l-fs-badfv-1-baden-b-junioren-landes-fs-b-junioren-saison1718-baden/-/staffel/0204M79BIK000000VS54898DVUL01S6C-D">FS/BJ/L-FS/BADFV/1</a>
						</div>
						<div class="label"></div>
					</div>
				</div>
				<div class="row">
					<div class="column-left">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/fs-bj-l-fs-swfv-1-suedwest-b-junioren-landes-fs-b-junioren-saison1718-suedwest/-/staffel/020604G778000000VS54898DVUL01S6C-D">FS/BJ/L-FS/SWFV/1</a>
						</div>
						<div class="label"></div>
					</div>
					<div class="column-right">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/fs-bj-r-fs-r-sfv-1-deutschland-b-junioren-regional-fs-b-junioren-saison1718-deutschland/-/staffel/0201RHS4Q0000000VS54898DVUL01S6C-D">FS/BJ/R-FS/R-SFV/1</a>
						</div>
						<div class="label"></div>
					</div>
				</div>
				<div class="row">
					<div class="column-left">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/fs-cj-r-fs-r-sfv-1-deutschland-c-junioren-regional-fs-c-junioren-saison1718-deutschland/-/staffel/0206ICBAJ0000000VS54898EVTOIL9QR-D">FS/CJ/R-FS/R-SFV/1</a>
						</div>
						<div class="label"></div>
					</div>
					<div class="column-right">
						<div class="value">
							<a href="http://www.fussball.de/spieltagsuebersicht/fs-f-b-fs-dfb-1-deutschland-frauen-freundschaftsspiele-frauen-saison1718-deutschland/-/staffel/01VTKR3HO8000000VS54898EVV57PUFP-D">FS/F/B-FS/DFB/1</a>
						</div>
						<div class="label"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="team-courts" class="profile-theme-blue" data-lazyload>
	<div class="team-courts">
		<div class="factfile factfile-dark">
			<div class="factfile-headline">
				<h3 class="headline">Spielstätten</h3>
			</div>
			<div class="factfile-data">
				<div class="row">
					<div class="column-left">
						<div class="value">01.07.2017 &#8203; 30.06.2018</div>
						<div class="label">Von - Bis</div>
					</div>
					<div class="column-right">
						<div class="value">
							<a href="https://www.google.de/maps?q=Schwetzinger+Str.+92%2C+69190+Walldorf" target="_blank">
								
									FCA Walldorf
									, 
									Schwetzinger Str. 92
									<br>
									69190
									&nbsp;
									Walldorf
								
							</a>
						</div>
						<div class="label">Adresse</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="teamFixturesMatchdayLeagueTable">
	<div id="team-fixture-league-tables-nav">
		<div data-ng-controller="AjaxController" class="team-table-filter-nav table-filter">
			<div class="row">
				<form data-ajax-type="html" data-ajax-trigger=".season-trigger" data-ajax-target="#team-fixture-league-tables-nav" data-ajax-resource="http://www.fussball.de/ajax.team.table.nav/-/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-ajax="replace" data-ajax-method="post">
					<div data-select-trigger-class="season-trigger" data-ng-model="ngSaisonX" data-ng-init="ngSaisonX='1718'" data-select-box="single" data-select-box-default="0" data-select-title="Saison" class="select-wrapper" data-ajaxmodel="saison">
						<select size="1" name="saison">
							<option value="1718" class="selected" selected="selected">2017/2018</option>
							<option value="1617">2016/2017</option>
							<option value="1516">2015/2016</option>
							<option value="1415">2014/2015</option>
							<option value="1314">2013/2014</option>
							<option value="1213">2012/2013</option>
							<option value="1112">2011/2012</option>
							<option value="1011">2010/2011</option>
							<option value="0910">2009/2010</option>
							<option value="0809">2008/2009</option>
							<option value="0708">2007/2008</option>
							<option value="0607">2006/2007</option>
							<option value="0506">2005/2006</option>
							<option value="0405">2004/2005</option>
						</select>
					</div>
					<div data-ng-model="ngStaffelX" data-ng-init="ngStaffelX='staffel'" data-select-box="single" data-select-box-default="0" data-select-title="Wettbewerb" class="select-wrapper" data-ajaxmodel="staffel">
						<select size="1" name="staffel">
							<option value="020EQ1DMQ8000003VS54898DVTQF3A0H-G" class="selected" selected="selected">bfv-B-Junioren Landesliga Rhein/Neckar</option>
						</select>
					</div>
					<button type="submit" class="button button-primary">Los</button>
				</form>
			</div>
		</div>
		<div data-toggle="li a" data-type="ajax" class="tab-group has-icons" data-tab-group>
			<ul>
				<li class="on">
					<a data-tracking-name="mannschaft_tabelle/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_tabelle" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-table"></span>Tabelle</a>
				</li>
				<li>
					<a data-tracking-name="mannschaft_hinrueck/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_hinrueck" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table.rounds/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table.rounds/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table.rounds/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-rounds"></span>Hin-/ Rückrunde</a>
				</li>
				<li>
					<a data-tracking-name="mannschaft_heimauswaerts/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_heimauswaerts" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table.home.away/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table.home.away/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table.home.away/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-home-away"></span>Heim/ Auswärts</a>
				</li>
				<li>
					<a data-tracking-name="mannschaft_fieberkurve/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_fieberkurve" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table.fevercurve/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table.fevercurve/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table.fevercurve/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-curve"></span>Fieberkurve</a>
				</li>
				<li>
					<a data-tracking-name="mannschaft_kreuztabelle/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_kreuztabelle" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table.cross/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table.cross/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table.cross/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-cross-table"></span>Kreuztabelle</a>
				</li>
				<li>
					<a data-tracking-name="mannschaft_fairness/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="html" data-tracking-pagename-long="mannschaft_fairness" data-ajax-target="#team-fixture-league-tables" data-ajax-resource="http://www.fussball.de/ajax.team.table.fairness/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.table.fairness/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.table.fairness/-/saison/0201IGL94G000000VS54898DVUL01S6C/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax><span class="icon-fairness"></span>Fairness</a>
				</li>
			</ul>
		</div>
		<div id="team-fixture-league-tables" class="table-container fixtures-league-table">
			<table class="table table-striped table-full-width">
				<thead>
					<tr class="thead">
						<th colspan="2"><span class="visible-small">Pl.</span><span class="hidden-small">Platz</span></th>
						<th class="column-large">Mannschaft</th>
						<th><span class="visible-small">Sp.</span><span class="hidden-small">Spiele</span></th>
						<th class="hidden-small">G</th>
						<th class="hidden-small">U</th>
						<th class="hidden-small">V</th>
						<th><span class="visible-small">Torv.</span><span class="hidden-small">Torverhältnis</span></th>
						<th class="hidden-small">Tordifferenz</th>
						<th><span class="visible-small">Pkt.</span><span class="hidden-small">Punkte</span></th>
					</tr>
				</thead>
				<tbody>
					<tr class="row-promotion own">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							1.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="FC Astoria Walldorf 2">
								</div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">14</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">0</td>
						<td class="no-wrap">105 : 9</td>
						<td class="hidden-small">96</td>
						<td class="column-points">42</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							2.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfl-kurpfalz-mannheim-neckarau-vfl-kurpfalz-mannheim-neckarau-baden/-/saison/1718/team-id/01E03IV450000000VV0AG811VTA8FO8N" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008RVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfL Kurpfalz Mannheim-Neckarau">
								</div>
								<div class="club-name">
									VfL Kurpfalz Mannheim-Neckarau
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">9</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">3</td>
						<td class="no-wrap">42 : 22</td>
						<td class="hidden-small">20</td>
						<td class="column-points">28</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							3.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/tsg-62-09-weinheim-tsg-62-09-weinheim-baden/-/saison/1718/team-id/011MICLQ1K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A8VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="TSG 62/09 Weinheim">
								</div>
								<div class="club-name">
									TSG 62/&#8203;09 Weinheim
								</div>
							</a>
						</td>
						<td>12</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">4</td>
						<td class="no-wrap">35 : 20</td>
						<td class="hidden-small">15</td>
						<td class="column-points">22</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							4.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-gartenstadt-vfb-gartenstadt-baden/-/saison/1718/team-id/011MIFD46K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008NVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfB Gartenstadt">
								</div>
								<div class="club-name">
									VfB Gartenstadt
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">6</td>
						<td class="no-wrap">42 : 50</td>
						<td class="hidden-small">-8</td>
						<td class="column-points">22</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-up-right"></span></td>
						<td class="column-rank">
							5.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-baiertal-schatthausen-spvgg-baiertal-baden/-/saison/1718/team-id/011MIB1C40000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006IVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Baiertal/Schatthausen">
								</div>
								<div class="club-name">
									SG Baiertal/&#8203;Schatthausen
								</div>
							</a>
						</td>
						<td>15</td>
						<td class="hidden-small">7</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">42 : 56</td>
						<td class="hidden-small">-14</td>
						<td class="column-points">21</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							6.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sv-98-schwetzingen-sv-98-schwetzingen-baden/-/saison/1718/team-id/011MIF5TEC000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A4VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SV 98 Schwetzingen">
								</div>
								<div class="club-name">
									SV 98 Schwetzingen
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">20 : 32</td>
						<td class="hidden-small">-12</td>
						<td class="column-points">16</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-up-right"></span></td>
						<td class="column-rank">
							7.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-waibstadt-meckesheim-moenchzell-daisbach-sg-waibstadt-baden/-/saison/1718/team-id/01SMKMQ6C8000000VS548985VU8O1RK1" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800005SVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Waibstadt/Meckesheim-Mönchzell/Daisbach">
								</div>
								<div class="club-name">
									SG Waibstadt/&#8203;Meckesheim-Mönchzell/&#8203;Daisbach
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">1</td>
						<td class="hidden-small">8</td>
						<td class="no-wrap">33 : 46</td>
						<td class="hidden-small">-13</td>
						<td class="column-points">16</td>
					</tr>
					<tr class="odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							8.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/tsg-91-09-luetzelsachsen-tsg-91-09-luetzelsachsen-baden/-/saison/1718/team-id/011MIC2U1G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800009QVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="TSG 91/09 Lützelsachsen">
								</div>
								<div class="club-name">
									TSG 91/&#8203;09 Lützelsachsen
								</div>
							</a>
						</td>
						<td>12</td>
						<td class="hidden-small">4</td>
						<td class="hidden-small">3</td>
						<td class="hidden-small">5</td>
						<td class="no-wrap">24 : 25</td>
						<td class="hidden-small">-1</td>
						<td class="column-points">15</td>
					</tr>
					<tr>
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							9.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-dossenheim-ziegelh-peterstal-1-fc-sportfr-dossenheim-baden/-/saison/1718/team-id/011MIC855G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006NVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="SG Dossenheim/Ziegelhausen-Peterstal">
								</div>
								<div class="club-name">
									SG Dossenheim/&#8203;Ziegelhausen-Peterstal
								</div>
							</a>
						</td>
						<td>14</td>
						<td class="hidden-small">5</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">9</td>
						<td class="no-wrap">21 : 58</td>
						<td class="hidden-small">-37</td>
						<td class="column-points">15</td>
					</tr>
					<tr class="row-relegation odd">
						<td class="column-icon"><span class="icon-arrow-down-right"></span></td>
						<td class="column-rank">
							10.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-eppingen-2-vfb-eppingen-baden/-/saison/1718/team-id/01A4655LQ4000000VV0AG811VSUI9EOJ" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800004VVV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="VfB Eppingen 2">
								</div>
								<div class="club-name">
									VfB Eppingen 2
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">4</td>
						<td class="hidden-small">2</td>
						<td class="hidden-small">7</td>
						<td class="no-wrap">37 : 33</td>
						<td class="hidden-small">4</td>
						<td class="column-points">14</td>
					</tr>
					<tr class="row-relegation">
						<td class="column-icon"><span class="icon-arrow-right"></span></td>
						<td class="column-rank">
							11.
						</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-zuzenhausen-fc-zuzenhausen-baden/-/saison/1718/team-id/01E0PF8DBG000000VV0AG80NVV2L7DJE" class="club-wrapper">
								<div class="club-logo table-image">
									<img src="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000060VV0AG08LVUPGND5I/verband/0123456789ABCDEF0123456700004180" alt="FC Zuzenhausen">
								</div>
								<div class="club-name">
									FC Zuzenhausen
								</div>
							</a>
						</td>
						<td>13</td>
						<td class="hidden-small">2</td>
						<td class="hidden-small">0</td>
						<td class="hidden-small">11</td>
						<td class="no-wrap">11 : 61</td>
						<td class="hidden-small">-50</td>
						<td class="column-points">6</td>
					</tr>
				</tbody>
			</table>
			<div data-toggle=".legend > span, .note > span" class="table-meta">
				<ul class="functions">
					<li class="legend"><span data-toggle-content=".table-legend">Legende<span class="icon-angle-down"></span></span></li>
					<li class="note"><span data-toggle-content=".tab-note">Hinweis zur Tabelle<span class="icon-angle-down"></span></span></li>
					<li class="print">
						<a href="http://www.fussball.de/mannschaft.spieltag.druck/-/max/999/mode/PRINT/staffel/020EQ1DMQ8000003VS54898DVTQF3A0H-G/team-id/011MIDI43O000000VTVG0001VTR8C1K7" target="_blank">Drucken<span class="icon-link-arrow"></span></a>
					</li>
				</ul>
				<div class="table-legend">
					<h3>Bereich "Kürzel bei der Mannschaft"</h3>
					<div class="row">
						<div class="wrapper">
							<div class="column">
								<div class="item"><span>oW</span></div>
								<div class="description">Diese Mannschaft spielt in dieser Staffel nicht mehr mit, die Ergebnisse werden aber eingerechnet</div>
							</div>
							<div class="column">
								<div class="item"><span>zg.</span></div>
								<div class="description">Diese Mannschaft wurde zurückgezogen, die Ergebnisse werden aber eingerechnet</div>
							</div>
							<div class="column">
								<div class="item"><span>SW</span></div>
								<div class="description">Für diese Mannschaft ist eine separate Sonderwertung eingerechnet</div>
							</div>
						</div>
					</div>
					<h3>Bereich Trend</h3>
					<div class="row">
						<div class="wrapper">
							<div class="column">
								<div class="item"><span class="icon-arrow-up-right"></span></div>
								<div class="description">Tabellenplatz hat sich im Vergleich zum vorherigen Spieltag verbessert</div>
							</div>
							<div class="column">
								<div class="item"><span class="icon-arrow-right"></span></div>
								<div class="description">Tabellenplatz bleibt im Vergleich zum vorherigen Spieltag unverändert</div>
							</div>
							<div class="column">
								<div class="item"><span class="icon-arrow-down-right"></span></div>
								<div class="description">Tabellenplatz hat sich im Vergleich zum vorherigen Spieltag verschlechtert</div>
							</div>
						</div>
					</div>
				</div>
				<div class="tab-note">
					<h3>Hinweis zur Tabellenrechnung</h3>
					<p>Der SKV Sandhofen hat seine Mannschaft vom Spielbetrieb zurück gezogen und steht somit als erster Absteiger fest !!  17.10.17 S.B.</p>
				</div>
			</div>
		</div>
	</div>
</section>


<section id="team-timeline" class="profile-theme-blue" data-lazyload>
	<div class="team-timeline">
		<div class="timeline">
			<div class="timeline-headline">
				<h3 class="headline">Wettbewerbe seit 04/05</h3>
				<p class="subline">Höchste Spielklasse: Landesliga</p>
			</div>
			<div class="timeline-content">
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">16/17</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">1. PLATZ</p>
							<p class="copy">Landesliga / bfv-B-Junioren Landesliga Rhein/Neckar</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">15/16</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">7. PLATZ</p>
							<p class="copy">Landesliga / bfv-B-Junioren Landesliga Rhein/Neckar</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">14/15</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">1. PLATZ</p>
							<p class="copy">Landesliga / bfv-B-Junioren Landesliga Rhein/Neckar</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">13/14</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">5. PLATZ</p>
							<p class="copy">Landesliga / bfv-B-Junioren Landesliga R/N</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">12/13</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">1. PLATZ</p>
							<p class="copy">Landesliga / bfv-B-Junioren Landesliga R/N</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">11/12</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">2. PLATZ</p>
							<p class="copy">Landesliga / B-Junioren Landesliga R/N</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">10/11</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">4. PLATZ</p>
							<p class="copy">Landesliga / B-Junioren Landesliga R/N</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">09/10</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">1. PLATZ</p>
							<p class="copy">Kreisliga / B-Junioren Kreisliga</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">08/09</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">9. PLATZ</p>
							<p class="copy">Landesliga / B-Junioren Landesliga R/N</p>
						</div>
					</div>
				</div>
				<div class="section">
					<div class="season">
						<div class="hexagon">
							<span class="icon-hexagon"></span>
							<div class="inner">
								<div class="valign-wrapper">
									<div class="valign-inner">Saison<span class="year">07/08</span></div>
								</div>
							</div>
						</div>
					</div>
					<div class="events">
						<div class="event">
							<p class="title">1. PLATZ</p>
							<p class="copy">Kreisliga / B-Junioren Kreisliga HD</p>
						</div>
					</div>
				</div>
			</div>
			<form data-ajax-type="html" data-ng-controller="AjaxController" data-ajax-target=".team-timeline" data-ajax-resource="http://www.fussball.de/ajax.team.timeline/-/load-more/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="load-more" data-ajax="replace" data-ajax-method="get" data-tracking="{'href':'http://www.fussball.de/ajax.team.timeline/-/load-more/true/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}">
				<button type="submit" class="load-more-button">Alle anzeigen<span class="icon-arrow-down"></span></button>
			</form>
		</div>
	</div>
</section>
<section id="teamStatsWin">
	<div data-toggle="li a" data-ng-controller="AjaxController" data-type="ajax" class="tab-group" data-tab-group>
		<ul>
			<li class="on">
				<a data-tracking-name="mannschaft_hoechste_siege/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="json" data-tracking-pagename-long="mannschaft_hoechste_siege" data-ajax-target="#team-stats" data-tracking-subchannel="statistik" data-ajax-resource="http://www.fussball.de/ajax.team.win/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.win/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.win/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Höchste Siege</a>
			</li>
			<li>
				<a data-tracking-name="mannschaft_torreichste_unentschieden/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="json" data-tracking-pagename-long="mannschaft_torreichste_unentschieden" data-ajax-target="#team-stats" data-tracking-subchannel="stats" data-ajax-resource="http://www.fussball.de/ajax.team.draw/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.draw/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.draw/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Torreichste Unentschieden</a>
			</li>
			<li>
				<a data-tracking-name="mannschaft_hoechste_niederlagen/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-pagename-short="mannschaft" data-tracking-channel="vereine_verbaende" data-ajax-type="json" data-tracking-pagename-long="mannschaft_hoechste_niederlagen" data-ajax-target="#team-stats" data-tracking-subchannel="stats" data-ajax-resource="http://www.fussball.de/ajax.team.loose/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" href="http://www.fussball.de/ajax.team.loose/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-tracking-enabled="" data-tracking="{'href':'http://www.fussball.de/ajax.team.loose/-/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}" data-ajax>Höchste Niederlagen</a>
			</li>
		</ul>
	</div>
	<div data-ng-controller="AjaxController" id="team-stats">
		<div class="table-container fixtures-matches-table club-matchplan-table">
			<table class="table table-striped table-full-width">
				<thead>
					<tr class="thead hidden-small">
						<th class="align-right"><span class="hidden-small inline">Datum |&nbsp;</span>Zeit</th>
						<th>Wettbewerb</th>
						<th class="hidden-small">Mannschaft</th>
						<th colspan="2">Heim</th>
						<th>Gast</th>
						<th><span class="hidden-small">Ergebnis</span><span class="visible-small">Erg.</span></th>
						<th><span class="visible-full">Info</span></th>
						<th></th>
						<th></th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 07.04.2018</td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span class="hidden-small inline">Sa, 07.04.18 |&nbsp;</span>11:00</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-dossenheim-ziegelh-peterstal-1-fc-sportfr-dossenheim-baden/-/saison/1718/team-id/011MIC855G000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Dossenheim/Ziegelhausen-Peterstal" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006NVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SG Dossenheim/&#8203;Ziegelhausen-Peterstal
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-dossenheim-ziegelh-peterstal-1/-/spiel/020GBC217K000000VS54898EVVII0TR2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE67C;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE68E;&#xE66D;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-dossenheim-ziegelh-peterstal-1/-/spiel/020GBC217K000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Dienstag, 13.09.2016</td>
					</tr>
					<tr>
						<td class="column-date"><span class="hidden-small inline">Di, 13.09.16 |&nbsp;</span>19:00</td>
						<td>Pokalspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/vfb-eberbach-vfb-eberbach-baden/-/saison/1617/team-id/011MIBCCJO000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="VfB Eberbach" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006PVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									VfB Eberbach
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1617/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-vfb-eberbach/-/spiel/01SUA281PC000000VS54898DVSPEV4E2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE6B0;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE65A;&#xE660;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-vfb-eberbach/-/spiel/01SUA281PC000000VS54898DVSPEV4E2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 17.09.2016</td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span class="hidden-small inline">Sa, 17.09.16 |&nbsp;</span>13:00</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/mfc-phoenix-02-mfc-phoenix-02-baden/-/saison/1617/team-id/011MICLT04000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="MFC Phönix Mannheim" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008BVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									MFC Phönix Mannheim
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1617/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-mfc-phoenix-02/-/spiel/01SQU12N5C000000VS54898EVUVJFG5P"><span data-obfuscation="wwaczkpz" class="score-left">&#xE69E;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE691;&#xE697;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-mfc-phoenix-02/-/spiel/01SQU12N5C000000VS54898EVUVJFG5P"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 16.09.2017</td>
					</tr>
					<tr>
						<td class="column-date"><span class="hidden-small inline">Sa, 16.09.17 |&nbsp;</span>15:15</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/sv-98-schwetzingen-sv-98-schwetzingen-baden/-/saison/1718/team-id/011MIF5TEC000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SV 98 Schwetzingen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B80000A4VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SV 98 Schwetzingen
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/sv-98-schwetzingen-fc-astoria-walldorf-2/-/spiel/020GBC1GTC000000VS54898EVVII0TR2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE678;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE66C;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/sv-98-schwetzingen-fc-astoria-walldorf-2/-/spiel/020GBC1GTC000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 25.11.2017</td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span class="hidden-small inline">Sa, 25.11.17 |&nbsp;</span>12:30</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/vfb-gartenstadt-vfb-gartenstadt-baden/-/saison/1718/team-id/011MIFD46K000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="VfB Gartenstadt" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800008NVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									VfB Gartenstadt
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/vfb-gartenstadt-fc-astoria-walldorf-2/-/spiel/020GBC26HG000000VS54898EVVII0TR2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE682;&#xE67F;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE65A;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/vfb-gartenstadt-fc-astoria-walldorf-2/-/spiel/020GBC26HG000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Dienstag, 03.10.2017</td>
					</tr>
					<tr>
						<td class="column-date"><span class="hidden-small inline">Di, 03.10.17 |&nbsp;</span>17:30</td>
						<td>Pokalspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-lobbach-1-sv-waldwimmersbach-baden/-/saison/1718/team-id/020D52MC1C000000VS548985VU5O2O7T" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Lobbach 1" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800007PVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SG Lobbach 1
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-lobbach-1/-/spiel/020JU0OD8O000000VS54898EVV27PHDA"><span data-obfuscation="wwaczkpz" class="score-left">&#xE6A9;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE6AA;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-lobbach-1/-/spiel/020JU0OD8O000000VS54898EVV27PHDA"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 25.03.2017</td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span class="hidden-small inline">Sa, 25.03.17 |&nbsp;</span>11:30</td>
						<td>Pokalspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1617/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/sg-nassig-sonderriet-sv-eintracht-nassig-baden/-/saison/1617/team-id/011MICE0A0000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Nassig/Sonderriet" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800000DVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SG Nassig/&#8203;Sonderriet
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/sg-nassig-sonderriet-fc-astoria-walldorf-2/-/spiel/01V2JOTD98000000VS54898DVV7I9SGS"><span data-obfuscation="wwaczkpz" class="score-left">&#xE695;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE68E;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/sg-nassig-sonderriet-fc-astoria-walldorf-2/-/spiel/01V2JOTD98000000VS54898DVV7I9SGS"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 08.04.2017</td>
					</tr>
					<tr>
						<td class="column-date"><span class="hidden-small inline">Sa, 08.04.17 |&nbsp;</span>12:00</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1617/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-zuzenhausen-fc-zuzenhausen-baden/-/saison/1617/team-id/01E0PF8DBG000000VV0AG80NVV2L7DJE" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Zuzenhausen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000060VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Zuzenhausen
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-zuzenhausen-fc-astoria-walldorf-2/-/spiel/01SQU12RV8000000VS54898EVUVJFG5P"><span data-obfuscation="wwaczkpz" class="score-left">&#xE691;&#xE67C;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE6B2;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-zuzenhausen-fc-astoria-walldorf-2/-/spiel/01SQU12RV8000000VS54898EVUVJFG5P"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Samstag, 11.11.2017</td>
					</tr>
					<tr class="odd">
						<td class="column-date"><span class="hidden-small inline">Sa, 11.11.17 |&nbsp;</span>12:45</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/sg-waibstadt-meckesheim-moenchzell-daisbach-sg-waibstadt-baden/-/saison/1718/team-id/01SMKMQ6C8000000VS548985VU8O1RK1" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Waibstadt/Meckesheim-Mönchzell/Daisbach" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800005SVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SG Waibstadt/&#8203;Meckesheim-Mönchzell/&#8203;Daisbach
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/sg-waibstadt-meckesheim-moenchzell-daisbach-fc-astoria-walldorf-2/-/spiel/020GBC16NO000000VS54898EVVII0TR2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE658;&#xE689;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE6B0;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/sg-waibstadt-meckesheim-moenchzell-daisbach-fc-astoria-walldorf-2/-/spiel/020GBC16NO000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
					<tr class="row-headline visible-small">
						<td colspan="11">Donnerstag, 21.09.2017</td>
					</tr>
					<tr>
						<td class="column-date"><span class="hidden-small inline">Do, 21.09.17 |&nbsp;</span>19:00</td>
						<td>Meisterschaftsspiel</td>
						<td class="column-team">B-Junioren</td>
						<td class="column-club">
							<a href="http://www.fussball.de/mannschaft/sg-baiertal-schatthausen-spvgg-baiertal-baden/-/saison/1718/team-id/011MIB1C40000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="SG Baiertal/Schatthausen" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B800006IVV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									SG Baiertal/&#8203;Schatthausen
								</div>
							</a>
						</td>
						<td class="strong no-border no-padding">:</td>
						<td class="column-club no-border">
							<a href="http://www.fussball.de/mannschaft/fc-astoria-walldorf-2-fc-astoria-walldorf-baden/-/saison/1718/team-id/011MIDI43O000000VTVG0001VTR8C1K7" class="club-wrapper">
								<div class="club-logo table-image"><span data-alt="FC Astoria Walldorf 2" data-responsive-image="//www.fussball.de/export.media/-/action/getLogo/format/3/id/00ES8GN9B8000083VV0AG08LVUPGND5I"></span></div>
								<div class="club-name">
									FC Astoria Walldorf 2
								</div>
							</a>
						</td>
						<td class="column-score">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-baiertal-schatthausen/-/spiel/020GBC1EJ0000000VS54898EVVII0TR2"><span data-obfuscation="wwaczkpz" class="score-left">&#xE69F;</span><span class="colon">:</span><span data-obfuscation="wwaczkpz" class="score-right">&#xE676;<span class="icon-verified"></span></span></a>
						</td>
						<td class="column-detail">
							<a href="http://www.fussball.de/spiel/fc-astoria-walldorf-2-sg-baiertal-schatthausen/-/spiel/020GBC1EJ0000000VS54898EVVII0TR2"><span class="icon-angle-right hidden-full"></span><span class="visible-full">Zum Spiel<span class="icon-link-arrow"></span></span></a>
						</td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
						<td class="column-detail fixture-media-info"></td>
					</tr>
				</tbody>
				<tfoot>
					<tr class="load-more">
						<td colspan="11">
							<form data-ajax-type="json" data-ajax-target="#team-stats" data-ajax-resource="http://www.fussball.de/ajax.team.win/-/load-more/true/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7" data-ajax="replace" data-tracking="{'href':'http://www.fussball.de/ajax.team.win/-/load-more/true/mime-type/JSON/team-id/011MIDI43O000000VTVG0001VTR8C1K7'}">
								<button type="submit" class="load-more-button">Alle anzeigen<span class="icon-arrow-down"></span></button>
							</form>
						</td>
					</tr>
				</tfoot>
			</table>
		</div>
	</div>
	<div data-toggle=".legend > span, .note > span" class="table-meta">
		<ul class="functions">
			<li class="legend"><span data-toggle-content=".table-legend">Legende<span class="icon-angle-down"></span></span></li>
			<li class="print">
				<a href="javascript: window.print();">Drucken<span class="icon-link-arrow"></span></a>
			</li>
		</ul>
		<div class="table-legend">
			<h3>Kürzel bei einem Spiel</h3>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>u</span></div>
						<div class="description">(U) Sportgerichtsurteil (bestätigt)</div>
					</div>
					<div class="column">
						<div class="item"><span>Annuliert</span></div>
						<div class="description">Annullierung</div>
					</div>
					<div class="column">
						<div class="item"><span>v</span></div>
						<div class="description">(V) Verwaltungsentscheid (bestätigt)</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>Absetzung</span></div>
						<div class="description">Spielabsetzung</div>
					</div>
					<div class="column">
						<div class="item"><span>w</span></div>
						<div class="description">(W) Wertung Spielinstanz (bestätigt)</div>
					</div>
					<div class="column">
						<div class="item"><span>Ausfall</span></div>
						<div class="description">Spielausfall</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>t</span></div>
						<div class="description">(T) Testspiel (bestätigt)</div>
					</div>
					<div class="column">
						<div class="item"><span>Abbruch</span></div>
						<div class="description">Spielabbruch</div>
					</div>
					<div class="column">
						<div class="item"><span>zg.</span></div>
						<div class="description">Diese Mannschaft wurde zurückgezogen, die Ergebnisse werden aber eingerechnet.</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>Nichtantritt BEIDE</span></div>
						<div class="description">nicht angetretene Mannschaften</div>
					</div>
					<div class="column">
						<div class="item"><span>Nichtantritt HEIM</span></div>
						<div class="description">nicht angetreten HEIM-Mannschaft</div>
					</div>
					<div class="column">
						<div class="item"><span>Nichtantritt GAST</span></div>
						<div class="description">nicht angetreten GAST-Mannschaft</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>nV</span></div>
						<div class="description">nach Verlängerung</div>
					</div>
					<div class="column">
						<div class="item"><span>nE</span></div>
						<div class="description">nach Elfmeterschießen</div>
					</div>
				</div>
			</div>
			<h3>Sonstiges</h3>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span>**</span></div>
						<div class="description">Die Anstoßzeit steht noch nicht fest oder ist nicht bekannt.</div>
					</div>
					<div class="column">
						<div class="item"><span>o.E.</span></div>
						<div class="description">Keine Ergebnisanzeige, da die Staffel nicht im Leistungsbetrieb spielt.</div>
					</div>
					<div class="column">
						<div class="item"><span>oW</span></div>
						<div class="description">Mannschaften mit diesem Kennzeichen spielen außer Konkurrenz.</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span class="icon-verified"></span></div>
						<div class="description">Ergebnis bestätigt</div>
					</div>
					<div class="column">
						<div class="item"><span>Live</span></div>
						<div class="description">Liveticker</div>
					</div>
					<div class="column">
						<div class="item"><span>SPIELFREI</span></div>
						<div class="description">An diesem Datum hat die Mannschaft spielfrei.</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="wrapper">
					<div class="column">
						<div class="item"><span class="icon-article"></span></div>
						<div class="description">Spielbericht vorhanden</div>
					</div>
					<div class="column">
						<div class="item"><span class="icon-foto"></span></div>
						<div class="description">Foto oder Video vorhanden</div>
					</div>
					<div class="column">
						<div class="item"><span class="icon-video"></span></div>
						<div class="description">Livestream oder Highlights vorhanden</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="teamProfile">
	<div data-toggle=".factfile-data .button-primary" data-toggle-content=".factfile-form" class="club-profile factfile" data-toggle-close=".link-close">
		<div class="factfile-headline">
			<h3 class="headline">
				<a href="http://www.fussball.de/verein/fc-astoria-walldorf-baden/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I">FC Astoria Walldorf</a>
			</h3>
			<p class="subline">
				<a href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180">Baden</a>
			</p>
		</div>
		<div class="factfile-data">
			<div class="row">
				<div class="column-left">
					<div class="value">1908</div>
					<div class="label">Gründungsjahr</div>
				</div>
				<div class="column-right">
					<div class="value">Blau-Weiß</div>
					<div class="label">Vereinsfarben</div>
				</div>
			</div>
			<div class="row">
				<div class="column-left">
					<div class="value">
						Schwetzinger Str. 92, 69190 Walldorf
					</div>
					<div class="label">Adresse</div>
				</div>
				<div class="column-right">
					<div class="value">&nbsp;</div>
					<div class="label">Ansprechpartner</div>
				</div>
			</div>
			<div class="row">
				<div class="column-left">
					<div class="value">
						<a href="http://www.fc-astoria-walldorf.de" target="_blank">www.fc-astoria-walldorf.de</a>
					</div>
					<div class="label">Website</div>
				</div>
				<div class="column-right">
					<button data-ajax-type="html" data-ajax-target=".contact-form-wrapper #captcha_1" data-ajax-resource="//www.fussball.de/ajax.captcha/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I" class="button button-primary" data-ajax-method="get" data-ajax>Verein kontaktieren</button>
				</div>
			</div>
		</div>
		<div class="factfile-form">
			<div class="inner">
				<a href="#" class="link-close"><span class="icon-close"></span></a>
				<form data-ajax-type="html" data-ng-controller="AjaxController" data-ajax-target=".contact-form-wrapper" data-ajax-resource="http://www.fussball.de/ajax.contact.form/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I" class="contact-form-wrapper" data-ajax="replace" data-ajax-method="post" data-tracking="{'href':'http://www.fussball.de/ajax.contact.form/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I'}">
					<div class="container">
						<p class="description">Nachricht an FC Astoria Walldorf</p>
					</div>
					<div class="container contact-form form-small">
						<div class="column-left">
							<input data-ng-model="ngFirstname" name="firstname" placeholder="Dein Vorname*" type="text" value="" class="input-firstname" data-ajaxmodel="firstname">
							<input data-ng-model="ngLastname" name="lastname" placeholder="Dein Nachname*" type="text" value="" class="input-lastname" data-ajaxmodel="lastname">
							<input data-ng-model="ngSender" name="address" placeholder="Deine E-Mail-Adresse*" type="text" value="" class="input-email" data-ajaxmodel="address">
							<input data-ng-model="ngSubject" name="subject" placeholder="Dein Betreff*" type="text" value="" class="input-subject" data-ajaxmodel="subject">
							<textarea data-ng-model="content" name="content" placeholder="Deine Nachricht*" data-ajaxmodel="content"></textarea>
						</div>
						<div class="column-right">
							<div id="captcha_1" class="captcha">
								<div>
									<img alt="renew captcha">
								</div>
								<a data-ajax-type="html" data-ajax-target=".contact-form-wrapper #captcha_1" data-ajax-resource="//www.fussball.de/ajax.captcha/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I" href="//www.fussball.de/ajax.captcha/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I" data-ajax-method="post" data-tracking="{'href':'//www.fussball.de/ajax.captcha/-/id/00ES8GN9B8000083VV0AG08LVUPGND5I'}" data-ajax><span class="icon-reload"></span></a>
								<input data-ng-model="digest" name="captcha-digest" type="hidden" value="" data-ajaxmodel="captcha-digest">
							</div>
							<input data-ng-model="securityCode" name="captcha-code" placeholder="Sicherheitscode*" type="text" value="" data-ajaxmodel="captcha-code">
							<button class="button button-primary">Nachricht senden</button>
							<p class="info">* Pflichtfelder</p>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</section>
<section data-ajaxcontent="http://service.media.fussball.de/api/comment/ajax/-/team/011MIDI43O000000VTVG0001VTR8C1K7" id="comments"></section>
<section id="news">
	<div class="news-list-related news-list">
		<div class="container grid-view">
			<ul>
				<li class="item nth1"><article class="news-article" >
                    <a href="/newsdetail/90-2-torwart-dahmen-trifft-per-hacke/-/article-id/184919">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_027f0868f8.jpg',
        																		'medium': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_3da102e27d.jpg',
        																		'large': 'fileadmin/_processed_/201804/csm_165081-Finn_Dahmen_4cbab2a1af.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Regionalliga Südwest


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 22:20
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>90.+2: Torwart Dahmen trifft per Hacke!</span>
        												</h2>
                            </div>
                            <p class="excerpt">Ein furioses Ende gab es beim 1:1 zwischen der zweiten Mannschaft des FSV Mainz 05 und der U 23 des VfB Stuttgart in einer Partie vom 27. Spieltag in der Regionalliga Südwest. In der Nachspielzeit gelang FSV-Torhüter Finn Dahmen per Hacke der Ausgleich. Der KSV Hessen Kassel fuhr beim TSV Steinbach den ersten Auswärtssieg nach 227 Tagen ein und der SV Röchling Völklingen unterlag 1899 Hoffenheim 1:2.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth2"><article class="news-article" >
                    <a href="/newsdetail/finaltag-der-amateure-22-klubs-schon-dabei/-/article-id/183677">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_2374543e9c.jpg',
        																		'medium': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_81e2a69843.jpg',
        																		'large': 'fileadmin/_processed_/201804/csm_165032-Bayreuth_Imago1_55d9267f9b.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                                    
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Magazin


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 13:40
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>Finaltag der Amateure: 22 Klubs schon dabei</span>
        												</h2>
                            </div>
                            <p class="excerpt">Alle Landespokalendspiele an einem Tag. Alle Landespokalendspiele live im Fernsehen. In einer siebenstündigen Konferenzschaltung, von der ARD bundesweit übertragen. Am 21. Mai geht der <i>Finaltag der Amateure</i> in seine dritte Runde. 22 Teilnehmer stehen bereits fest. <strong>FUSSBALL.DE</strong> gibt den Überblick.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth3"><article class="news-article" >
                    <a href="/newsdetail/traum-dfb-pokal-landespokale-im-ueberblick/-/article-id/172840">
                        
                                
                                    
                                            <span data-responsive-image="" data-src-folder="/assets/-/" data-src="{
                                            'small': 'fileadmin/_processed_/201708/csm_148053-123_3ae87edf42.jpg',
        																		'medium': 'fileadmin/_processed_/201708/csm_148053-123_57b36a8d48.jpg',
        																		'large': 'fileadmin/_dfbdam/148053-123.jpg'
        																		}"
        																		>
        																		</span>
                                        
                                
                            
                        <div class="article-content">
                            <div class="meta">
                                
                                        <span class="category">
                                        	<!-- categories -->

		Service


                                        </span>
                                        <span class="date">
                                        	11.04.2018 | 07:00
                                        </span>
                                    
                            </div>
                            <div class="headline">
                                <h2>
        													<span>Traum DFB-Pokal: Landespokale im Überblick</span>
        												</h2>
                            </div>
                            <p class="excerpt">Über die Landespokale haben auch die Amateurvereine in ganz Deutschland die Chance auf den <i>Finaltag der Amateure</i> und die große Bühne im DFB-Pokal. Sieben Endspielpaarungen stehen bereits fest. <strong>FUSSBALL.DE</strong> gibt den aktuellen Überblick über alle Landespokalwettbewerbe.</p>
                            <p class="read-more">Mehr lesen
                                <span class="icon-link-arrow"></span></p>
                        </div>
                    </a>
                </article></li>
				<li class="item nth4">
					<div class="news-teaser-two-rows">
						<a style="background-image: url(http://www.fussball.de/static/cms/6.80.99.3077/images/news/activitystream/teaser_association_bg1_300x300.jpg);" href="http://www.fussball.de/verband/baden/-/verband/0123456789ABCDEF0123456700004180">
							<div class="teaser-row">
								<div class="teaser-cell">
									<div class="category"><span>Landesverband</span></div>
									<span class="icon-hexagon"><img src="//www.fussball.de/export.media/-/action/getLogo/format/9/id/0123456789ABCDEF0123456700004180" alt="Baden"></span>
								</div>
							</div>
							<div class="teaser-row">
								<div class="teaser-cell">
									<p class="large">Badischer Fußball-Verband</p>
									<p class="link">Zum Verband</p>
								</div>
							</div>
						</a>
					</div>
				</li>
				<li class="item nth5"><div class="news-teaser-default" style="background-image: url(/assets/-/id/aufstellungsgrafik-409x430.jpg);">
	<a href="http://www.fussball.de/newsdetail/der-grosse-ueberblick-alles-zu-fussballde/-/article-id/116306">
		<div class="inner">
			<p class="large">
				Spitzenspiel.
				<br>
				Spitzen-Look.
			</p>
			<p class="link">Alles rund um FUSSBALL.DE</p>
		</div>
	</a>
</div></li>
				<li data-ajaxcontent="http://www.fussball.de/ajax.stats.amateur.teaser/-/max/5/stats/4/verband/0123456789ABCDEF0123456700004180" class="item nth6"></li>
			</ul>
		</div>
	</div>
</section>
			<section>
	<div class="cookie-advise">
		<div class="container">
			<div class="cookie-advise-content">
				<h3>Cookie Richtlinie</h3>
				<p>Um FUSSBALL.DE benutzerfreundlich zu gestalten, setzen wir Cookies ein. Cookies sind kleine Dateien, die vom Browser verwaltet und für einen späteren Abruf bereitgehalten werden, um die Nutzung von FUSSBALL.DE zu ermöglichen oder zu erleichtern. Sie dienen auch dazu um notwendige Statistiken zu erstellen. Teilweise werden auch Cookies von Dritten (z.B. Google und Facebook) eingesetzt. Mit der weiteren Nutzung unserer Dienste erklärst du dich damit einverstanden, dass wir Cookies verwenden. Du kannst die Cookie-Einstellung auch selbst verändern.  <span class="cookie-advise-content-link-container"><a href="http://www.fussball.de/privacy" class="cookie-advise-content-link">Mehr über unsere Cookies kannst du hier erfahren</a><span class="icon-link-arrow"></span></span></p>
			</div>
			<div class="cookie-advise-links">
				<a href="http://www.fussball.de/cookie.settings" class="cookie-advise-link cookie-advise-settings">Cookie-Einstellungen<span class="icon-link-arrow"></span></a>
				<span data-ng-click="setAllCookies()" class="cookie-advise-link cookie-advise-accept" data-cookie-setting>Cookies akzeptieren</span>
			</div>
		</div>
	</div>
</section>
		</div>
		<footer>
	<div id="sharing" class="visible-small">
		<h6>Teile diese Seite</h6>
		<ul>
			<li class="whatsapp mobile-only">
				<a href="" data-share-page="whatsapp" target="_blank"><span class="icon-whatsapp"></span></a>
			</li>
			<li class="facebook">
				<a href="" data-share-page="facebook" target="_blank"><span class="icon-facebook"></span></a>
			</li>
			<li class="twitter">
				<a href="" data-share-page="twitter" target="_blank"><span class="icon-twitter"></span></a>
			</li>
			<li class="googleplus">
				<a href="" data-share-page="googleplus" target="_blank"><span class="icon-googleplus"></span></a>
			</li>
		</ul>
	</div>
	<div class="footer-partner">
		<div class="container">
			<ul>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_oddset.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_coba.png">
					</a>
				</li>
				<li class="hidden-small">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_post.png">
					</a>
				</li>
				<li class="visible-small">
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_post_small.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_adidas.png">
					</a>
				</li>
				<li>
					<a href="http://www.fussball.de/partner">
						<img src="//www.fussball.de/static/layout/fbde2/por/6.80.99.3077/images/partner/footer_partner_logo_coca_cola.png">
					</a>
				</li>
			</ul>
		</div>
	</div>
	<div class="footer-meta-links">
		<div class="container">
			<nav class="metalinks">
				<ul>
					<li>
						<a href="http://www.fussball.de/imprint">Impressum</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/contact">Kontakt</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/privacy">Datenschutz</a>
					</li>
				</ul>
				<ul>
					<li>
						<a href="http://www.fussball.de/terms.and.conditions">Nutzungsbedingungen</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/youth.protection">Jugendschutz</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/content.responsibility">Inhalteverantwortung</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://www.fussball.de/cookie.settings">Cookies</a>
						<span class="divider">&#124;</span>
					</li>
					<li>
						<a href="http://training-service.fussball.de/faq/">FAQ</a>
					</li>
				</ul>
			</nav>
			<div class="copyright">&copy; DFB</div>
		</div>
	</div>
	<div class="footer-slogan" data-adjust-footer-slogan-height>
		<div class="container"><span class="footer-slogan-text">Die Heimat des Amateurfussballs</span><span class="footer-slogan-logo"><img src="http://www.fussball.de/static/layout/fbde2/por/6.80.99.3077/font/logo.svg" alt="" width="24" class="logo-graphic" height="16"><span class="logo-letters">fussball.de</span></span></div>
	</div>
</footer>
		
		
	<div data-ajaxsurvey="//www.fussball.de/ajax.survey/-/path/_path_" data-survey-path-variable="_path_" data-survey="survey-1" id="ajax-survey"></div>
		


		
		<script type="text/javascript" nonce="" src="//www.fussball.de/static/por/6.80.99.3077/js/script.js"></script>
		
		<data-enable-tracking></data-enable-tracking>
	</body>
</html>




'''

ver_urls = []

#----------------------Vereins URL--------------------------------------------------------------------------------

soup = BeautifulSoup(html,'lxml')
for link in soup.find_all('a', {'class': "club-wrapper"}):
    if link.get('href')!= None:
        ver_urls.append(link.get('href'))

#-----------------------Vereinsseite Scrapen------------------------------------------------------------------------


asoup = BeautifulSoup(ahtml, 'lxml')
title = asoup.find("title").get_text()
print(title)

aso = asoup.find(id="teamProfile")
a = aso.find_all('div', {'class': "column-left"})

b=a[1].find('div',{'class': "value"})
b=b.text
b=b.replace('\t', '')
print(b)

#r = requests.get(ver_urls[0])
#data = r.content

#print(data.decode("utf8"))

'''
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:


parsed_html = BeautifulSoup(html)
print parsed_html.body.find('div', attrs={'class':'container'}).text


#clubname = tree.xpath('//div[@class="club-name"]/text()')

#for c in clubname:
   # print(c)

#pprint.pprint(clubname)
'''