
TREEHERDER_URL = 'https://treeherder.mozilla.org/#/jobs'
DATAZILLA_URL_TEMPLATE = 'https://datazilla.mozilla.org/refdata/pushlog/list/?days_ago=%(days)s&branches=%(branch)s'
HOST_ALERT_MANAGER = 'http://alertmanager.allizom.org:8080'

TREES = ('Mozilla-Inbound',
         'Mozilla-Inbound-Non-PGO',
         'Fx-Team',
         'Fx-Team-Non-PGO',
         'Firefox',
         'Firefox-Non-PGO',
         'Mozilla-Aurora',
         'Mozilla-Aurora-Non-PGO',
         'Mozilla-Beta',
         'Mozilla-Beta-Non-PGO',
         'B2g-Inbound',
         'B2g-Inbound-Non-PGO',
         'mobile')


# jmaher: I don't care too much about centOS- that is builders
#             'CentOS release 5 (Final)', 'CentOS (x86_64) release 5 (Final)'

PLATFORMS = ('XP', 'Win7', 'Ubuntu HW 12.04 x64', 'Ubuntu HW 12.04', 'Linux',
             'WINNT 5.2', 'WINNT 6.1 (ix)', 'WINNT 6.2 x64', 'WINNT 5.1 (ix)',
             'MacOSX 10.7', 'MacOSX 10.8', 'MacOSX 10.6 (rev4)', 'Android 4.0.4')


TBPL_PLATFORMS = {
    'WINNT 5.1 (ix)': 'Windows XP 32-bit',
    'WINNT 5.2': '',
    'WINNT 6.1 (ix)': 'Windows 7 32-bit',
    'WINNT 6.2 x64': 'Windows 8 64-bit',
    'Ubuntu HW 12.04': 'Ubuntu HW 12.04',
    'Ubuntu HW 12.04 x64': 'Ubuntu HW 12.04 x64',
    'MacOSX 10.6 (rev4)': 'Rev4 MacOSX Snow Leopard 10.6',
    'MacOSX 10.8': 'Rev5 MacOSX Mountain Lion 10.8',
    'Android 4.0.4': 'Android 4.0 Tegra'
}


# oh the hacks continue, osx runs on the pgo branch without the pgo tag
TBPL_TREES = {
    'Mozilla-Inbound': 'mozilla-inbound pgo',
    'Mozilla-Inbound-Non-PGO': 'mozilla-inbound',
    'Fx-Team': 'fx-team pgo',
    'Fx-Team-Non-PGO': 'fx-team',
    'Firefox': 'mozilla-central pgo',
    'Firefox-Non-PGO': 'mozilla-central',
    'Mozilla-Aurora': 'mozilla-aurora pgo',
    'Mozilla-Aurora-Non-PGO': 'mozilla-aurora',
    'Mozilla-Beta': 'mozilla-beta pgo',
    'Mozilla-Beta-Non-PGO': 'mozilla-beta',
    'B2g-Inbound': 'b2g-inbound pgo',
    'B2g-Inbound-Non-PGO': 'b2g-inbound',
    'mobile': 'mozilla-central'
}


TBPL_TESTS = {
    'SVG No Chrome': {'testname': 'tsvgx', 'wikiname': 'tsvg.2C_tsvgx', 'jobname': 'svgr'},
    'SVG Row Major': {'testname': 'tsvgx', 'wikiname': 'tsvg.2C_tsvgx', 'jobname': 'svgr'},
    'SVG, Opacity Row Major': {'testname': 'tsvgr_opacity', 'wikiname': 'tsvg-opacity', 'jobname': 'svgr'},
    'Dromaeo (DOM)': {'testname': 'dromaeo_dom', 'wikiname': 'Dromaeo_DOM', 'jobname': 'dromaeojs'},
    'Dromaeo (CSS)': {'testname': 'dromaeo_css', 'wikiname': 'Dromaeo_CSS', 'jobname': 'dromaeojs'},
    'Kraken Benchmark': {'testname': 'kraken', 'wikiname': 'kraken', 'jobname': 'dromaeojs'},
    'V8': {'testname': 'v8_7', 'wikiname': 'V8.2C_version_7', 'jobname': 'dromaeojs'},
    'V8 Version 7': {'testname': 'v8_7', 'wikiname': 'V8.2C_version_7', 'jobname': 'dromaeojs'},
    'V8 version 7': {'testname': 'v8_7', 'wikiname': 'V8.2C_version_7', 'jobname': 'dromaeojs'},
    'Paint': {'testname': 'tpaint', 'wikiname': 'tpaint', 'jobname': 'other'},
    'tscroll Row Major': {'testname': 'tscrollx', 'wikiname': 'tscroll.2C_tscrollx', 'jobname': 'svgr'},
    'TResize': {'testname': 'tresize', 'wikiname': 'tresize', 'jobname': 'chromez'},
    'Tp5 Optimized': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized (Private Bytes)': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized (Main RSS)': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized (Content RSS)': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized (%CPU)': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 No Network Row major MozAfterPaint (Main Startup File I/O Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 No Network Row Major MozAfterPaint (Non-Main Startup File IO Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 No Network Row Major MozAfterPaint (Non-Main Normal Network IO Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 No Network Row Major MozAfterPaint (Main Normal File IO Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 No Network Row Major MozAfterPaint (Main Startup File IO Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 No Network Row Major MozAfterPaint (Non-Main Normal File IO Bytes)': {'testname': 'tp5n', 'wikiname': 'xperf', 'jobname': 'xperf'},
    'Tp5 Optimized (Modified Page List Bytes)': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized Responsiveness': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'Tp5 Optimized MozAfterPaint': {'testname': 'tp5o', 'wikiname': 'tp5', 'jobname': 'tp5o'},
    'a11y Row Major MozAfterPaint': {'testname': 'a11yr', 'wikiname': 'a11y', 'jobname': 'other'},
    'Tp4 Mobile': {'testname': 'tp4m', 'wikiname': 'tp5', 'jobname': 'remote-tp4m_nochrome'},
    'LibXUL Memory during link': {'testname': '', 'wikiname': '', 'jobname': ''},
    'Ts, Paint': {'testname': 'ts_paint', 'wikiname': 'ts_paint', 'jobname': 'other'},
    'Robocop Pan Benchmark': {'testname': 'trobopan', 'wikiname': 'robocop', 'jobname': 'remote-trobopan'},
    'Robocop Database Benchmark': {'testname': '', 'wikiname': 'robocop', 'jobname': 'remote-troboprovider'},
    'Robocop Checkerboarding No Snapshot Benchmark': {'testname': 'tcheckerboard', 'wikiname': 'robocop', 'jobname': 'remote-trobocheck2'},
    'Robocop Checkerboarding Real User Benchmark': {'testname': 'tcheck2', 'wikiname': 'robocop', 'jobname': 'remote-trobocheck2'},
    'Customization Animation Tests': {'testname': 'cart', 'wikiname': 'TART.2FCART', 'jobname': 'svgr'},
    'Latency Performance Tests': {'testname': '', 'wikiname': '', 'jobname': ''},
    'Tab Animation Test, NoChrome': {'testname': 'tart', 'wikiname': 'TART.2FCART', 'jobname': 'svgr'},
    'Tab Animation Test': {'testname': 'tart', 'wikiname': 'TART.2FCART', 'jobname': 'svgr'},
    'Canvasmark, NoChrome': {'testname': 'tcanvasmark', 'wikiname': 'CanvasMark', 'jobname': 'chromez'},
    'Canvasmark': {'testname': 'tcanvasmark', 'wikiname': 'CanvasMark', 'jobname': 'chromez'},
    'CanvasMark, NoChrome': {'testname': 'tcanvasmark', 'wikiname': 'CanvasMark', 'jobname': 'chromez'},
    'CanvasMark': {'testname': 'tcanvasmark', 'wikiname': 'CanvasMark', 'jobname': 'chromez'},
    'Tab Animation Test, NoChrome': {'testname': 'tart', 'wikiname': 'TART.2FCART', 'jobname': 'svgr'},
    'tscroll-ASAP': {'testname': 'tscrollx', 'wikiname': 'tscroll.2C_tscrollx', 'jobname': 'svgr'},
    'SVG-ASAP, NoChrome': {'testname': 'tsvgx', 'wikiname': 'tsvg.2C_tsvgx', 'jobname': 'svgr'},
    'SVG-ASAP': {'testname': 'tsvgx', 'wikiname': 'tsvg.2C_tsvgx', 'jobname': 'svgr'},
    'tscroll-ASAP MozAfterPaint': {'testname': 'tscrollx', 'wikiname': 'tscroll.2C_tscrollx', 'jobname': 'svgr'},
    'Session Restore no Auto Restore Test': {'testname': 'sessionrestore_no_auto_restore', 'wikiname': 'sessionrestore.2Fsessionrestore_no_auto_restore', 'jobname': 'other'},
    'Session Restore Test': {'testname': 'sessionrestore', 'wikiname': 'sessionrestore.2Fsessionrestore_no_auto_restore', 'jobname': 'other'},
    'WebRTC Media Performance Tests': {'testname': 'media_tests', 'wikiname': 'media_tests', 'jobname': 'other'},
    'TP5 Scroll': {'testname': 'tp5o_scroll', 'wikiname': 'tp5o_scroll', 'jobname': 'g1'},
    'WEBGL Terrain': {'testname': 'glterrain', 'wikiname': 'glterrain', 'jobname': 'g1'}
}


TESTS = (
    'SVG No Chrome',
    'SVG Row Major',
    'SVG, Opacity Row Major',
    'Dromaeo (DOM)',
    'Dromaeo (CSS)',
    'Kraken Benchmark',
    'V8',
    'V8 Version 7',
    'V8 version 7',
    'Paint',
    'tscroll Row Major',
    'TResize',
    'Tp5 Optimized',
    'Tp5 Optimized (Private Bytes)',
    'Tp5 Optimized (Main RSS)',
    'Tp5 Optimized (Content RSS)',
    'Tp5 Optimized (%CPU)',
    'Tp5 No Network Row major MozAfterPaint (Main Startup File I/O Bytes)',
    'Tp5 No Network Row Major MozAfterPaint (Non-Main Startup File IO Bytes)',
    'Tp5 No Network Row Major MozAfterPaint (Non-Main Normal Network IO Bytes)',
    'Tp5 No Network Row Major MozAfterPaint (Main Normal File IO Bytes)',
    'Tp5 No Network Row Major MozAfterPaint (Main Startup File IO Bytes)',
    'Tp5 Optimized (Modified Page List Bytes)',
    'Tp5 Optimized Responsiveness',
    'Tp5 Optimized MozAfterPaint',
    'a11y Row Major MozAfterPaint',
    'Tp4 Mobile',
    'LibXUL Memory during link',
    'Ts, Paint',
    'Robocop Pan Benchmark',
    'Robocop Database Benchmark',
    'Robocop Checkerboarding No Snapshot Benchmark',
    'Robocop Checkerboarding Real User Benchmark',
    'Customization Animation Tests',
    'Latency Performance Tests',
    'Tab Animation Test, NoChrome',
    'Tab Animation Test',
    'Canvasmark, NoChrome',
    'Canvasmark',
    'CanvasMark, NoChrome',
    'CanvasMark',
    'Tab Animation Test, NoChrome',
    'tscroll-ASAP',
    'SVG-ASAP, NoChrome',
    'SVG-ASAP',
    'tscroll-ASAP MozAfterPaint',
    'Session Restore no Auto Restore Test',
    'Session Restore Test',
    'TP5 Scroll',
    'WEBGL Terrain',
    'WebRTC Media Performance Tests')