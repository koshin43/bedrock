from bedrock.redirects.util import redirect, is_firefox_redirector, no_redirect


def firefox_mobile_faq(request, *args, **kwargs):
    qs = request.META.get('QUERY_STRING', '')
    if 'os=firefox-os' in qs:
        return 'https://support.mozilla.org/products/firefox-os'

    return 'firefox.android.faq'


redirectpatterns = (
    # overrides
    redirect('^zh-TW/mobile/?', 'http://mozilla.com.tw/firefox/mobile/', locale_prefix=False),
    redirect('^zh-TW/download/?', 'http://mozilla.com.tw/firefox/download/', locale_prefix=False),

    redirect(r'^firefox/aurora/all/?$', 'firefox.all', to_kwargs={'channel': 'developer'}),

    # bug 831810 & 1142583 & 1239960
    redirect(r'^mwc/?$', 'firefox.os.devices', re_flags='i', query={
        'utm_campaign': 'mwc-redirect',
        'utm_medium': 'referral',
        'utm_source': 'mozilla.org',
    }),

    # bug 748503
    redirect(r'^projects/firefox/[^/]+a[0-9]+/firstrun(?P<p>.*)$',
             '/firefox/nightly/firstrun{p}'),

    # bug 1275483
    redirect(r'^firefox/nightly/whatsnew/?', 'firefox.nightly_firstrun'),

    # bug 840814
    redirect(r'^projects/firefox'
             r'(?P<version>/(?:\d+\.\d+\.?(?:\d+)?\.?(?:\d+)?(?:[a|b]?)(?:\d*)(?:pre)?(?:\d)?))'
             r'(?P<page>/(?:firstrun|whatsnew))'
             r'(?P<rest>/.*)?$', '/firefox{version}{page}{rest}'),

    # bug 877165
    redirect(r'^firefox/connect', 'mozorg.home'),

    # bug 657049, 1238851
    redirect(r'^firefox/accountmanager/?$', 'https://developer.mozilla.org/Persona'),

    # bug 841846
    redirect(r'^firefox/nightly/?$', 'https://nightly.mozilla.org/'),

    # Bug 1009247, 1101220
    redirect(r'^((firefox|mobile)/)?beta/?$', 'firefox.channel', anchor='beta'),
    redirect(r'^((firefox|mobile)/)?aurora/?$', 'firefox.channel', anchor='developer'),

    # bug 988044
    redirect(r'^firefox/unsupported-systems\.html$', 'firefox.unsupported-systems'),

    # bug 736934, 860865, 1101220, 1153351
    redirect(r'^mobile/(?P<channel>(?:beta|aurora)/)?notes/?$',
             '/firefox/android/{channel}notes/'),
    redirect(r'^firefox/(?P<channel>(?:beta|aurora|organizations)/)?system-requirements(\.html)?$',
             '/firefox/{channel}system-requirements/'),

    # bug 1155870
    redirect(r'^firefox/os/(releases|notes)/?$',
             'https://developer.mozilla.org/Firefox_OS/Releases'),
    redirect(r'^firefox/os/(?:release)?notes/(?P<v>[^/]+)/?$',
             'https://developer.mozilla.org/Firefox_OS/Releases/{v}'),

    # bug 878871
    redirect(r'^firefoxos', '/firefox/os/'),

    # Bug 1006616
    redirect(r'^download/?$', 'firefox.new'),

    # bug 837883
    redirect(r'^firefox/firefox\.exe$', 'mozorg.home', re_flags='i'),

    # bug 821006
    redirect(r'^firefox/all(\.html)?$', 'firefox.all'),

    # bug 727561
    redirect(r'^firefox/search(?:\.html)?$', 'firefox.new'),

    # bug 860865, 1101220
    redirect(r'^firefox/all-(?:beta|rc)(?:/|\.html)?$', 'firefox.all',
             to_kwargs={'channel': 'beta'}),
    redirect(r'^firefox/all-aurora(?:/|\.html)?$', 'firefox.all',
             to_kwargs={'channel': 'developer'}),
    redirect(r'^firefox/aurora/(?P<page>all|notes|system-requirements)/?$',
             '/firefox/developer/{page}/'),
    redirect(r'^firefox/organizations/all\.html$', 'firefox.all',
             to_kwargs={'channel': 'organizations'}),

    # bug 729329
    redirect(r'^mobile/sync', 'firefox.sync'),

    # bug 882845
    redirect(r'^firefox/toolkit/download-to-your-devices', 'firefox.new'),

    # bug 1014823
    redirect(r'^(products/)?firefox/releases/whatsnew/?$', 'firefox.whatsnew'),

    # bug 929775
    redirect(r'^firefox/update', 'firefox.new', query={
        'utm_source': 'firefox-browser',
        'utm_medium': 'firefox-browser',
        'utm_campaign': 'firefox-update-redirect',
    }),

    # Bug 868182, 986174
    redirect(r'^(m|(firefox/)?mobile)/features/?$', 'firefox.android.index'),
    redirect(r'^(m|(firefox/)?mobile)/faq/?$', firefox_mobile_faq, query=False),

    # bug 884933
    redirect(r'^(m|(firefox/)?mobile)/platforms/?$',
             'https://support.mozilla.org/kb/will-firefox-work-my-mobile-device'),

    redirect(r'^m/?$', 'firefox.new'),

    # Bug 730488 deprecate /firefox/all-older.html
    redirect(r'^firefox/all-older\.html$', 'firefox.new'),

    # bug 1120658
    redirect(r'^seamonkey-transition\.html$',
             'http://www-archive.mozilla.org/seamonkey-transition.html'),

    # Bug 1186373
    redirect(r'^firefox/hello/npssurvey/?$',
             'https://www.surveygizmo.com/s3/2227372/Firefox-Hello-Product-Survey',
             permanent=False),

    # Bug 1221739
    redirect(r'^firefox/hello/feedbacksurvey/?$',
             'https://www.surveygizmo.com/s3/2319863/d2b7dc4b5687',
             permanent=False),

    # bug 1148127
    redirect(r'^products/?$', 'firefox.family.index'),

    # Bug 1110927
    redirect(r'^(products/)?firefox/start/central\.html$', 'firefox.new'),
    redirect(r'^firefox/sync/firstrun\.html$', 'firefox.sync'),
    redirect(r'^firefox/panorama/?$', 'https://support.mozilla.org/kb/tab-groups-organize-tabs'),

    # Bug 920212
    redirect(r'^firefox/fx/?$', 'firefox.new'),

    # Bug 979531, 1003727, 979664, 979654, 979660
    redirect(r'^firefox/customize/?$', 'firefox.desktop.customize'),
    redirect(r'^firefox/(?:performance|happy|speed|memory)/?$', 'firefox.desktop.fast'),
    redirect(r'^firefox/security/?$', 'firefox.desktop.trust'),
    redirect(r'^firefox/technology/?$', 'https://developer.mozilla.org/docs/Tools'),

    # Bug 979527
    redirect(r'^(products/)?firefox/central(/|\.html|-lite\.html)?$', is_firefox_redirector(
        'https://support.mozilla.org/kb/get-started-firefox-overview-main-features',
        'firefox.new'), cache_timeout=0),

    # bug 868169
    redirect(r'^mobile/android-download\.html$',
             'https://play.google.com/store/apps/details',
             query={'id': 'org.mozilla.firefox'}, merge_query=True),
    redirect(r'^mobile/android-download-beta\.html$',
             'https://play.google.com/store/apps/details',
             query={'id': 'org.mozilla.firefox_beta'}, merge_query=True),

    # bug 675031
    redirect(r'^projects/fennec(?P<page>/[\/\w\.-]+)?',
             'http://website-archive.mozilla.org/www.mozilla.org/fennec_releasenotes/projects/fennec{page}'),

    # bug 876581
    redirect(r'^firefox/phishing-protection(/?)$',
             'https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work'),

    # bug 1006079
    redirect(r'^mobile/home/?(?:index.html)?$',
             'https://blog.mozilla.org/services/2012/08/31/retiring-firefox-home/'),

    # bug 949562
    redirect(r'^mobile/home/1\.0/releasenotes(?:/(?:index.html)?)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_home/mobile/home/1.0/releasenotes/'),
    redirect(r'^mobile/home/1\.0\.2/releasenotes(?:/(?:index.html)?)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_home/mobile/home/1.0.2/releasenotes/'),
    redirect(r'^mobile/home/faq(?:/(?:index.html)?)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_home/mobile/home/faq/'),

    # bug 960064
    redirect(r'^firefox/(?P<num>vpat-[.1-5]+)(?:\.html)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_vpat/firefox-{num}.html'),
    redirect(r'^firefox/vpat(?:\.html)?',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_vpat/firefox-vpat-3.html'),

    # bug 1017564
    redirect(r'^mobile/.+/system-requirements/?$',
             'https://support.mozilla.org/kb/will-firefox-work-my-mobile-device'),

    # bug 858315
    redirect(r'^projects/devpreview/firstrun(?:/(?:index.html)?)?$', '/firefox/firstrun/'),
    redirect(r'^projects/devpreview/(?P<page>[\/\w\.-]+)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/devpreview_releasenotes/projects/devpreview/{page}'),

    # bug 1001238, 1025056
    no_redirect(r'^firefox/(24\.[5678]\.\d|28\.0)/releasenotes/?$'),

    # bug 1235082
    no_redirect(r'^firefox/23\.0(\.1)?/releasenotes/?$'),

    # bug 947890, 1069902
    redirect(r'^firefox/releases/(?P<v>[01]\.(?:.*))$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/firefox/releases/{v}'),
    redirect(r'^(?P<path>(?:firefox|mobile)/(?:\d)\.(?:.*)/releasenotes(?:.*))$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US/{path}'),
    #
    # bug 988746, 989423, 994186, 1153351
    redirect(r'^mobile/(?P<v>2[38]\.0(?:\.\d)?|29\.0(?:beta|\.\d)?)/releasenotes/?$',
             '/firefox/android/{v}/releasenotes/'),
    redirect(r'^mobile/(?P<v>[3-9]\d\.\d(?:a2|beta|\.\d)?)/(?P<p>aurora|release)notes/?$',
             '/firefox/android/{v}/{p}notes/'),

    # bug 1041712, 1069335, 1069902
    redirect(r'^(?P<prod>firefox|mobile)/(?P<vers>([0-9]|1[0-9]|2[0-8])\.(\d+(?:beta|a2|\.\d+)?))'
             r'/(?P<channel>release|aurora)notes/(?P<page>[\/\w\.-]+)?$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes/en-US'
             '/{prod}/{vers}/{channel}notes/{page}'),

    # bug 767614 superceeded by bug 957711 and 1003718 and 1239960
    redirect(r'^(mobile|fennec)/?$', 'firefox.family.index'),

    # bug 876668
    redirect(r'^mobile/customize(?:/.*)?$', '/firefox/android/'),

    # bug 1211907
    redirect(r'^firefox/independent/?$', 'firefox.new'),
    redirect(r'^firefox/personal/?$', 'firefox.new'),

    # bug 845983
    redirect(r'^metrofirefox(?P<path>/.*)?$', '/firefox{path}'),

    # bug 1003703, 1009630
    redirect(r'^firefox(?P<vers>/.+)/firstrun/eu/?$', '/firefox{vers}/firstrun/', query={
        'utm_source': 'direct',
        'utm_medium': 'none',
        'utm_campaign': 'redirect',
        'utm_content': 'eu-firstrun-redirect',
    }),

    # bug 960543
    redirect(r'^firefox/(?P<vers>[23])\.0/eula', '/legal/eula/firefox-{vers}/'),

    # bug 1224060
    redirect(
        r'^ja/firefox/ios/(?P<vers>[0-9]+(\.[0-9]+)*)/(?P<file>releasenotes|system-requirements)',
        'https://www.mozilla.jp/firefox/ios/{vers}/{file}/', locale_prefix=False),

    # bug 1150713
    redirect(r'^firefox/sms(?:/.*)?$', 'firefox.family.index'),

    # Redirects for SeaMonkey project website, now living at seamonkey-project.org
    redirect(r'^projects/seamonkey/$', 'http://www.seamonkey-project.org/'),
    redirect(r'^projects/seamonkey/artwork\.html$',
             'http://www.seamonkey-project.org/dev/artwork'),
    redirect(r'^projects/seamonkey/community\.html$',
             'http://www.seamonkey-project.org/community'),
    redirect(r'^projects/seamonkey/get-involved\.html$',
             'http://www.seamonkey-project.org/dev/get-involved'),
    redirect(r'^projects/seamonkey/index\.html$', 'http://www.seamonkey-project.org/'),
    redirect(r'^projects/seamonkey/news\.html$', 'http://www.seamonkey-project.org/news'),
    redirect(r'^projects/seamonkey/project-areas\.html$',
             'http://www.seamonkey-project.org/dev/project-areas'),
    redirect(r'^projects/seamonkey/releases/$', 'http://www.seamonkey-project.org/releases/'),
    redirect(r'^projects/seamonkey/releases/index\.html$',
             'http://www.seamonkey-project.org/releases/'),
    redirect(r'^projects/seamonkey/review-and-flags\.html$',
             'http://www.seamonkey-project.org/dev/review-and-flags'),
    redirect(r'^projects/seamonkey/releases/(?P<vers>1\..*)\.html$',
             'http://www.seamonkey-project.org/releases/{vers}'),
    redirect(r'^projects/seamonkey/releases/seamonkey(?P<x>.*)/index.html$',
             'http://www.seamonkey-project.org/releases/seamonkey{x}/'),
    redirect(r'^projects/seamonkey/releases/seamonkey(?P<x>.*/.*).html$',
             'http://www.seamonkey-project.org/releases/seamonkey{x}'),
    redirect(r'^projects/seamonkey/releases/updates/(?P<x>.*)$',
             'http://www.seamonkey-project.org/releases/updates/{x}'),
    redirect(r'^projects/seamonkey/start/$', 'http://www.seamonkey-project.org/start/'),

    # Bug 638948 redirect beta privacy policy link
    redirect(r'^firefox/beta/feedbackprivacypolicy/?$', '/privacy/firefox/'),

    # Bug 1238248
    redirect(r'^firefox/push/?$',
             'https://support.mozilla.org/kb/push-notifications-firefox'),

    # Bug 1239960
    redirect(r'^firefox/partners/?$', 'firefox.os.index'),

    # Bug 1243060
    redirect(r'^firefox/tiles/?$',
             'https://support.mozilla.org/kb/about-tiles-new-tab'),

    # Bug 1239863
    redirect(r'^firefox/os/1\.1/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/1\.3/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/1\.3t/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/1\.4/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/2\.0/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/2\.5/?$', 'firefox.os.index'),
    redirect(r'^firefox/os/faq/?$',
             'https://support.mozilla.org/products/firefox-os'),

    # Bug 1252332
    redirect(r'^sync/?$', 'firefox.sync'),

    # Bug 424204
    redirect(r'^firefox/help/?$', 'https://support.mozilla.com/{locale}kb/'),

    redirect(r'^fxandroid/?$', 'firefox.android.index'),

    # Bug 1255882
    redirect(r'^firefox/personal', 'firefox.new'),
    redirect(r'^firefox/upgrade', 'firefox.new'),
    redirect(r'^firefox/ie', 'firefox.new'),

    # must go above the bug 1255882 stuff below
    redirect('^projects/xul/joy-of-xul\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Tech/XUL/The_Joy_of_XUL'),
    redirect('^projects/xul/xre(old)?\.html$',
             'https://developer.mozilla.org/docs/Archive/Mozilla/XULRunner'),
    redirect('^projects/xslt/js-interface\.html$',
             'https://developer.mozilla.org/docs/'
             'Web/XSLT/Using_the_Mozilla_JavaScript_interface_to_XSL_Transformations'),
    redirect('^projects/xslt/faq\.html$',
             'https://developer.mozilla.org/docs/'
             'Web/API/XSLTProcessor/XSL_Transformations_in_Mozilla_FAQ'),
    redirect('^projects/xslt/standalone\.html$',
             'https://developer.mozilla.org/docs/'
             'Archive/Mozilla/Building_TransforMiiX_standalone'),
    redirect('^projects/plugins/first-install-problem\.html$',
             'https://developer.mozilla.org/Add-ons/Plugins/The_First_Install_Problem'),
    redirect('^projects/plugins/install-scheme\.html$',
             'https://developer.mozilla.org/docs/'
             'Installing_plugins_to_Gecko_embedding_browsers_on_Windows'),
    redirect('^projects/plugins/npruntime-sample-in-visual-studio\.html$',
             'https://developer.mozilla.org/docs/'
             'Compiling_The_npruntime_Sample_Plugin_in_Visual_Studio'),
    redirect('^projects/plugins/npruntime\.html$',
             'https://developer.mozilla.org/docs/Plugins/Guide/Scripting_plugins'),
    redirect('^projects/plugins/plugin-host-control\.html$',
             'https://developer.mozilla.org/docs/'
             'Archive/Mozilla/ActiveX_Control_for_Hosting_Netscape_Plug-ins_in_IE'),
    redirect('^projects/plugins/xembed-plugin-extension\.html$',
             'https://developer.mozilla.org/Add-ons/Plugins/XEmbed_Extension_for_Mozilla_Plugins'),
    redirect('^projects/netlib/http/http-debugging\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Debugging/HTTP_logging'),
    redirect('^projects/netlib/integrated-auth\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Integrated_authentication'),
    redirect('^projects/netlib/Link_Prefetching_FAQ\.html$',
             'https://developer.mozilla.org/docs/Web/HTTP/Link_prefetching_FAQ'),
    redirect(r'^projects/embedding/GRE\.html$',
             'https://developer.mozilla.org/docs/Archive/Mozilla/GRE'),
    redirect(r'^projects/embedding/windowAPIs\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Tech/Embedded_Dialog_API'),
    redirect(r'^projects/embedding/howto/config\.html$',
             'https://developer.mozilla.org/docs/Gecko/Embedding_Mozilla/Roll_your_own_browser'),
    redirect(r'^projects/embedding/howto/Initializations\.html$',
             'https://developer.mozilla.org/docs/Gecko/Embedding_Mozilla/Roll_your_own_browser'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasicsTOC\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics#toc'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics2\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics#Why_Gecko'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics3\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#What_You_Need_to_Embed'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics4\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#Getting_the_Code'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics5\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#Understanding_the_Coding_Environment'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics6\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics#XPCOM'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics7\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics#XPIDL'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics8\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#XPConnect_and_XPT_files'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics9\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#String_classes'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics10\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics#XUL.2FXBL'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics11\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#Choosing_Additional_Functionalities'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics12\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#What_Gecko_Provides'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics13\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#What_You_Provide'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics14\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#Common_Embedding_Tasks'),
    redirect(r'^projects/embedding/embedoverview/EmbeddingBasics16\.html$',
             'https://developer.mozilla.org/docs/Mozilla/Gecko/Gecko_Embedding_Basics'
             '#Appendix:_Data_Flow_Inside_Gecko'),
    redirect(r'^projects/embedding/examples/',
             'https://developer.mozilla.org/docs/Gecko/Embedding_Mozilla/Roll_your_own_browser'),

    # Bug 1255882
    redirect(r'^projects/bonecho/anti-phishing/?$',
             'https://support.mozilla.org/kb/how-does-phishing-and-malware-protection-work'),
    redirect(r'^projects/bonecho(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/bonsai(/.*)?$', 'https://wiki.mozilla.org/Bonsai'),
    redirect(r'^projects/camino(/.*)?$', 'http://caminobrowser.org/'),
    redirect(r'^projects/cck(/.*)?$', 'https://wiki.mozilla.org/CCK'),
    redirect(r'^projects/chimera(/.*)?$', 'http://caminobrowser.org/'),
    redirect(r'^projects/deerpark(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/embedding/faq\.html$',
             'https://developer.mozilla.org/docs/Gecko/Embedding_Mozilla/FAQ/How_do_I...'),
    redirect(r'^projects/embedding(/.*)?$',
             'https://developer.mozilla.org/docs/Gecko/Embedding_Mozilla'),
    redirect(r'^projects/granparadiso(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/inspector/faq\.html$',
             'https://developer.mozilla.org/docs/Tools/Add-ons/DOM_Inspector/DOM_Inspector_FAQ'),
    redirect(r'^projects/inspector(/.*)?$',
             'https://developer.mozilla.org/docs/Tools/Add-ons/DOM_Inspector'),
    redirect(r'^projects/javaconnect(/.*)?$',
             'http://developer.mozilla.org/en/JavaXPCOM'),
    redirect(r'^projects/minefield(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/minimo(/.*)?$', 'https://wiki.mozilla.org/Mobile'),
    redirect(r'^projects/namoroka(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/nspr(?:/.*)?$', 'https://developer.mozilla.org/docs/NSPR'),
    redirect(r'^projects/netlib(/.*)?$',
             'https://developer.mozilla.org/docs/Mozilla/Projects/Necko'),
    redirect(r'^projects/plugins(/.*)?$', 'https://developer.mozilla.org/Add-ons/Plugins'),
    redirect(r'^projects/rt-messaging(/.*)?$', 'http://chatzilla.hacksrus.com/'),
    redirect(r'^projects/shiretoko(/.*)?$', 'firefox.channel'),
    redirect(r'^projects/string(/.*)?$',
             'https://developer.mozilla.org/en/XPCOM_string_guide'),
    redirect(r'^projects/tech-evangelism(/.*)?$',
             'https://wiki.mozilla.org/Evangelism'),
    redirect(r'^projects/venkman(/.*)?$',
             'https://developer.mozilla.org/docs/Archive/Mozilla/Venkman'),
    redirect(r'^projects/webservices/examples/babelfish-wsdl(/.*)?$',
             'https://developer.mozilla.org/docs/SOAP_in_Gecko-based_Browsers'),
    redirect(r'^projects/xbl(/.*)?$', 'https://developer.mozilla.org/docs/Mozilla/Tech/XBL'),
    redirect(r'^projects/xforms(/.*)?$', 'https://developer.mozilla.org/docs/Archive/Web/XForms'),
    redirect(r'^projects/xpcom(/.*)?$', 'https://developer.mozilla.org/docs/Mozilla/Tech/XPCOM'),
    redirect(r'^projects/xpinstall(/.*)?$',
             'https://developer.mozilla.org/docs/Archive/Mozilla/XPInstall'),
    redirect(r'^projects/xslt(/.*)?$', 'https://developer.mozilla.org/docs/Web/XSLT'),
    redirect(r'^projects/xul(/.*)?$', 'https://developer.mozilla.org/docs/Mozilla/Tech/XUL'),
    redirect(r'^quality/help(/.*)?$', 'http://quality.mozilla.org/get-involved'),
    redirect(r'^quality(/.*)?$', 'http://quality.mozilla.org/'),

    # Bug 654614 /blocklist -> addons.m.o/blocked
    redirect(r'^blocklist(/.*)?$', 'https://addons.mozilla.org/blocked/'),

    redirect('^products/firebird$', 'firefox.family.index'),
    redirect('^products/firebird/download/$', 'firefox.new'),
    redirect('^products/firefox/add-engines\.html$',
             'https://addons.mozilla.org/search-engines.php'),
    redirect('^products/firefox/all$', '/firefox/all/'),
    redirect('^products/firefox/all\.html$', '/firefox/all/'),
    redirect('^products/firefox/banners\.html$', '/contribute/friends/'),
    redirect('^products/firefox/buttons\.html$', '/contribute/friends/'),
    redirect('^products/firefox/download', 'firefox.new'),
    redirect('^products/firefox/get$', 'firefox.new'),
    redirect('^products/firefox/$', 'firefox.family.index'),
    redirect('^products/firefox/live-bookmarks', '/firefox/features/'),
    redirect('^products/firefox/mirrors\.html$', 'http://www-archive.mozilla.org/mirrors.html'),
    redirect('^products/firefox/releases/$', '/firefox/releases/'),
    redirect('^products/firefox/releases/0\.9\.2\.html$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes'
             '/en-US/firefox/releases/0.9.1.html'),
    redirect('^products/firefox/releases/0\.10\.1\.html$',
             'http://website-archive.mozilla.org/www.mozilla.org/firefox_releasenotes'
             '/en-US/firefox/releases/0.10.html'),
    redirect('^products/firefox/search', '/firefox/features/'),
    redirect('^products/firefox/shelf\.html$', 'https://blog.mozilla.org/press/awards/'),
    redirect('^products/firefox/smart-keywords\.html$',
             'https://support.mozilla.org/en-US/kb/Smart+keywords'),
    redirect('^products/firefox/support/$', 'https://support.mozilla.org/'),
    redirect('^products/firefox/switch', 'firefox.new'),
    redirect('^products/firefox/system-requirements', '/firefox/system-requirements/'),
    redirect('^products/firefox/tabbed-browsing', 'firefox.desktop.index'),
    redirect('^products/firefox/text-zoom\.html$',
             'https://support.mozilla.org/kb/font-size-and-zoom-increase-size-of-web-pages'),
    redirect('^products/firefox/themes$', 'https://addons.mozilla.org/themes/'),
    redirect('^products/firefox/themes\.html$', 'https://addons.mozilla.org/themes/'),
    redirect('^products/firefox/ui-customize\.html$',
             'https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars'),
    redirect('^products/firefox/upgrade', 'firefox.new'),
    redirect('^products/firefox/why/$', 'firefox.desktop.index'),

    # bug 857246 redirect /products/firefox/start/  to start.mozilla.org
    redirect(r'^products/firefox/start/?$', 'http://start.mozilla.org'),
    redirect(r'^products/firefox', 'firefox.family.index'),

    # bug 1260423
    redirect(r'^firefox/choose/?$', 'firefox.new'),

    # bug 1283397
    redirect(r'^firefox/pocket/?$', 'https://getpocket.com/firefox/'),

    # bug 1288552 - redirect /secondrun/ traffic from funnelcake test
    redirect(r'^firefox(?:\/\d+\.\d+(?:\.\d+)?(?:a\d+)?)?/secondrun(?:/.*)?',
             'firefox.mobile-download', query=False),

    # bug 1293539
    redirect(r'^firefox(?:\/\d+\.\d+(?:\.\d+)?(?:a\d+)?)?/tour/?$',
             'https://support.mozilla.org/kb/get-started-firefox-overview-main-features'),

    # bug 1295332
    redirect(r'^hello/?$', 'https://support.mozilla.org/kb/hello-status'),
    redirect(r'^firefox/hello/?$', 'https://support.mozilla.org/kb/hello-status'),
    redirect(r'^firefox(?:\/\d+\.\d+(?:\.\d+)?(?:a\d+)?)?/hello/start/?$', 'https://support.mozilla.org/kb/hello-status'),
)
