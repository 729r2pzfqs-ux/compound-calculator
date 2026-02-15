import os

translations = {
    'de': {
        'lang': 'de', 'locale': 'de_DE', 'flag': '🇩🇪', 'name': 'Deutsch',
        'title': 'Zinseszinsrechner | Kostenloser Investitionsrechner',
        'desc': 'Kostenloser Zinseszinsrechner. Sehen Sie, wie Ihre Investitionen mit täglicher, monatlicher oder jährlicher Verzinsung wachsen.',
        'h1': 'Zinseszins<span class="text-emerald-400">rechner</span>',
        'subtitle': 'Sehen Sie, wie Ihr Geld im Laufe der Zeit wächst',
        'enter_details': 'Geben Sie Ihre Daten ein',
        'initial': 'Anfangsinvestition', 'monthly': 'Monatlicher Beitrag',
        'rate': 'Jährlicher Zinssatz', 'period': 'Zeitraum', 'years': 'Jahre',
        'frequency': 'Zinsfrequenz', 'daily': 'Täglich', 'monthly_freq': 'Monatlich',
        'quarterly': 'Vierteljährlich', 'annually': 'Jährlich',
        'calculate': 'Wachstum berechnen 📊',
        'future_value': 'Endwert', 'total_interest': 'Gesamtzinsen',
        'total_deposits': 'Gesamteinzahlungen', 'interest_earned': 'Verdiente Zinsen',
        'growth': 'Wachstum im Zeitverlauf', 'vs_simple': 'Zinseszins vs Einfacher Zins',
        'simple': 'Einfacher Zins', 'compound': 'Zinseszins',
        'extra': 'Sie verdienen {amount} mehr mit Zinseszins!',
        'what_is': 'Was ist Zinseszins?',
        'what_desc': 'Zinseszins ist der Zins, der auf das Anfangskapital und auch auf die angesammelten Zinsen aus früheren Perioden berechnet wird.'
    },
    'es': {
        'lang': 'es', 'locale': 'es_ES', 'flag': '🇪🇸', 'name': 'Español',
        'title': 'Calculadora de Interés Compuesto | Calculadora de Inversiones Gratis',
        'desc': 'Calculadora gratuita de interés compuesto. Vea cómo crecen sus inversiones con capitalización diaria, mensual o anual.',
        'h1': 'Calculadora de Interés <span class="text-emerald-400">Compuesto</span>',
        'subtitle': 'Vea cómo crece su dinero con el tiempo',
        'enter_details': 'Ingrese sus datos',
        'initial': 'Inversión Inicial', 'monthly': 'Aporte Mensual',
        'rate': 'Tasa de Interés Anual', 'period': 'Período de Tiempo', 'years': 'años',
        'frequency': 'Frecuencia de Capitalización', 'daily': 'Diario', 'monthly_freq': 'Mensual',
        'quarterly': 'Trimestral', 'annually': 'Anual',
        'calculate': 'Calcular Crecimiento 📊',
        'future_value': 'Valor Futuro', 'total_interest': 'Interés Total',
        'total_deposits': 'Depósitos Totales', 'interest_earned': 'Interés Ganado',
        'growth': 'Crecimiento a lo Largo del Tiempo', 'vs_simple': 'Compuesto vs Interés Simple',
        'simple': 'Interés Simple', 'compound': 'Interés Compuesto',
        'extra': '¡Gana {amount} más con interés compuesto!',
        'what_is': '¿Qué es el Interés Compuesto?',
        'what_desc': 'El interés compuesto es el interés calculado sobre el capital inicial y también sobre los intereses acumulados de períodos anteriores.'
    },
    'fr': {
        'lang': 'fr', 'locale': 'fr_FR', 'flag': '🇫🇷', 'name': 'Français',
        'title': 'Calculateur d\'Intérêts Composés | Calculateur d\'Investissement Gratuit',
        'desc': 'Calculateur gratuit d\'intérêts composés. Voyez comment vos investissements croissent avec une capitalisation quotidienne, mensuelle ou annuelle.',
        'h1': 'Calculateur d\'Intérêts <span class="text-emerald-400">Composés</span>',
        'subtitle': 'Voyez comment votre argent croît au fil du temps',
        'enter_details': 'Entrez vos données',
        'initial': 'Investissement Initial', 'monthly': 'Contribution Mensuelle',
        'rate': 'Taux d\'Intérêt Annuel', 'period': 'Période', 'years': 'ans',
        'frequency': 'Fréquence de Capitalisation', 'daily': 'Quotidien', 'monthly_freq': 'Mensuel',
        'quarterly': 'Trimestriel', 'annually': 'Annuel',
        'calculate': 'Calculer la Croissance 📊',
        'future_value': 'Valeur Future', 'total_interest': 'Intérêts Totaux',
        'total_deposits': 'Dépôts Totaux', 'interest_earned': 'Intérêts Gagnés',
        'growth': 'Croissance au Fil du Temps', 'vs_simple': 'Composé vs Intérêt Simple',
        'simple': 'Intérêt Simple', 'compound': 'Intérêt Composé',
        'extra': 'Vous gagnez {amount} de plus avec les intérêts composés!',
        'what_is': 'Qu\'est-ce que l\'Intérêt Composé?',
        'what_desc': 'L\'intérêt composé est l\'intérêt calculé sur le capital initial et également sur les intérêts accumulés des périodes précédentes.'
    },
    'pt': {
        'lang': 'pt', 'locale': 'pt_BR', 'flag': '🇧🇷', 'name': 'Português',
        'title': 'Calculadora de Juros Compostos | Calculadora de Investimentos Grátis',
        'desc': 'Calculadora gratuita de juros compostos. Veja como seus investimentos crescem com capitalização diária, mensal ou anual.',
        'h1': 'Calculadora de Juros <span class="text-emerald-400">Compostos</span>',
        'subtitle': 'Veja como seu dinheiro cresce ao longo do tempo',
        'enter_details': 'Digite seus dados',
        'initial': 'Investimento Inicial', 'monthly': 'Contribuição Mensal',
        'rate': 'Taxa de Juros Anual', 'period': 'Período', 'years': 'anos',
        'frequency': 'Frequência de Capitalização', 'daily': 'Diário', 'monthly_freq': 'Mensal',
        'quarterly': 'Trimestral', 'annually': 'Anual',
        'calculate': 'Calcular Crescimento 📊',
        'future_value': 'Valor Futuro', 'total_interest': 'Juros Totais',
        'total_deposits': 'Depósitos Totais', 'interest_earned': 'Juros Ganhos',
        'growth': 'Crescimento ao Longo do Tempo', 'vs_simple': 'Composto vs Juros Simples',
        'simple': 'Juros Simples', 'compound': 'Juros Compostos',
        'extra': 'Você ganha {amount} a mais com juros compostos!',
        'what_is': 'O que são Juros Compostos?',
        'what_desc': 'Juros compostos são os juros calculados sobre o capital inicial e também sobre os juros acumulados de períodos anteriores.'
    },
    'zh': {
        'lang': 'zh', 'locale': 'zh_CN', 'flag': '🇨🇳', 'name': '中文',
        'title': '复利计算器 | 免费投资增长计算器',
        'desc': '免费复利计算器。查看您的投资如何通过每日、每月或每年复利增长。',
        'h1': '复利<span class="text-emerald-400">计算器</span>',
        'subtitle': '查看您的资金如何随时间增长',
        'enter_details': '输入您的详细信息',
        'initial': '初始投资', 'monthly': '每月投入',
        'rate': '年利率', 'period': '投资期限', 'years': '年',
        'frequency': '复利频率', 'daily': '每日', 'monthly_freq': '每月',
        'quarterly': '每季度', 'annually': '每年',
        'calculate': '计算增长 📊',
        'future_value': '未来价值', 'total_interest': '总利息',
        'total_deposits': '总存款', 'interest_earned': '赚取的利息',
        'growth': '随时间增长', 'vs_simple': '复利 vs 单利',
        'simple': '单利', 'compound': '复利',
        'extra': '使用复利您可以多赚 {amount}！',
        'what_is': '什么是复利？',
        'what_desc': '复利是基于本金和之前期间累积利息计算的利息。它通常被称为"利滚利"，使您的资金增长比单利更快。'
    },
    'ja': {
        'lang': 'ja', 'locale': 'ja_JP', 'flag': '🇯🇵', 'name': '日本語',
        'title': '複利計算機 | 無料投資成長計算機',
        'desc': '無料の複利計算機。日次、月次、年次の複利で投資がどのように成長するかをご覧ください。',
        'h1': '複利<span class="text-emerald-400">計算機</span>',
        'subtitle': '時間とともにお金がどのように増えるかを見る',
        'enter_details': '詳細を入力',
        'initial': '初期投資額', 'monthly': '毎月の積立額',
        'rate': '年利率', 'period': '期間', 'years': '年',
        'frequency': '複利頻度', 'daily': '毎日', 'monthly_freq': '毎月',
        'quarterly': '四半期ごと', 'annually': '毎年',
        'calculate': '成長を計算 📊',
        'future_value': '将来価値', 'total_interest': '総利息',
        'total_deposits': '総預金額', 'interest_earned': '獲得利息',
        'growth': '時間経過による成長', 'vs_simple': '複利 vs 単利',
        'simple': '単利', 'compound': '複利',
        'extra': '複利で {amount} 多く稼げます！',
        'what_is': '複利とは？',
        'what_desc': '複利とは、元本と過去の期間に蓄積された利息の両方に対して計算される利息です。'
    },
    'hi': {
        'lang': 'hi', 'locale': 'hi_IN', 'flag': '🇮🇳', 'name': 'हिन्दी',
        'title': 'चक्रवृद्धि ब्याज कैलकुलेटर | मुफ्त निवेश कैलकुलेटर',
        'desc': 'मुफ्त चक्रवृद्धि ब्याज कैलकुलेटर। देखें कि आपका निवेश दैनिक, मासिक या वार्षिक चक्रवृद्धि के साथ कैसे बढ़ता है।',
        'h1': 'चक्रवृद्धि ब्याज <span class="text-emerald-400">कैलकुलेटर</span>',
        'subtitle': 'देखें कि समय के साथ आपका पैसा कैसे बढ़ता है',
        'enter_details': 'अपना विवरण दर्ज करें',
        'initial': 'प्रारंभिक निवेश', 'monthly': 'मासिक योगदान',
        'rate': 'वार्षिक ब्याज दर', 'period': 'समय अवधि', 'years': 'वर्ष',
        'frequency': 'चक्रवृद्धि आवृत्ति', 'daily': 'दैनिक', 'monthly_freq': 'मासिक',
        'quarterly': 'त्रैमासिक', 'annually': 'वार्षिक',
        'calculate': 'वृद्धि की गणना करें 📊',
        'future_value': 'भविष्य मूल्य', 'total_interest': 'कुल ब्याज',
        'total_deposits': 'कुल जमा', 'interest_earned': 'अर्जित ब्याज',
        'growth': 'समय के साथ वृद्धि', 'vs_simple': 'चक्रवृद्धि vs साधारण ब्याज',
        'simple': 'साधारण ब्याज', 'compound': 'चक्रवृद्धि ब्याज',
        'extra': 'चक्रवृद्धि ब्याज से आप {amount} अधिक कमाते हैं!',
        'what_is': 'चक्रवृद्धि ब्याज क्या है?',
        'what_desc': 'चक्रवृद्धि ब्याज वह ब्याज है जो प्रारंभिक मूलधन और पिछली अवधियों से संचित ब्याज दोनों पर गणना की जाती है।'
    },
    'ar': {
        'lang': 'ar', 'locale': 'ar_SA', 'flag': '🇸🇦', 'name': 'العربية',
        'title': 'حاسبة الفائدة المركبة | حاسبة الاستثمار المجانية',
        'desc': 'حاسبة الفائدة المركبة المجانية. شاهد كيف تنمو استثماراتك مع المضاعفة اليومية أو الشهرية أو السنوية.',
        'h1': 'حاسبة الفائدة <span class="text-emerald-400">المركبة</span>',
        'subtitle': 'شاهد كيف ينمو مالك بمرور الوقت',
        'enter_details': 'أدخل بياناتك',
        'initial': 'الاستثمار الأولي', 'monthly': 'المساهمة الشهرية',
        'rate': 'معدل الفائدة السنوي', 'period': 'الفترة الزمنية', 'years': 'سنوات',
        'frequency': 'تكرار المضاعفة', 'daily': 'يومياً', 'monthly_freq': 'شهرياً',
        'quarterly': 'ربع سنوي', 'annually': 'سنوياً',
        'calculate': 'احسب النمو 📊',
        'future_value': 'القيمة المستقبلية', 'total_interest': 'إجمالي الفائدة',
        'total_deposits': 'إجمالي الودائع', 'interest_earned': 'الفائدة المكتسبة',
        'growth': 'النمو عبر الزمن', 'vs_simple': 'مركبة vs فائدة بسيطة',
        'simple': 'فائدة بسيطة', 'compound': 'فائدة مركبة',
        'extra': 'تكسب {amount} أكثر مع الفائدة المركبة!',
        'what_is': 'ما هي الفائدة المركبة؟',
        'what_desc': 'الفائدة المركبة هي الفائدة المحسوبة على رأس المال الأصلي وأيضاً على الفائدة المتراكمة من الفترات السابقة.',
        'rtl': True
    },
    'ru': {
        'lang': 'ru', 'locale': 'ru_RU', 'flag': '🇷🇺', 'name': 'Русский',
        'title': 'Калькулятор Сложных Процентов | Бесплатный Инвестиционный Калькулятор',
        'desc': 'Бесплатный калькулятор сложных процентов. Посмотрите, как растут ваши инвестиции с ежедневным, ежемесячным или годовым начислением.',
        'h1': 'Калькулятор <span class="text-emerald-400">Сложных Процентов</span>',
        'subtitle': 'Посмотрите, как ваши деньги растут со временем',
        'enter_details': 'Введите ваши данные',
        'initial': 'Начальные Инвестиции', 'monthly': 'Ежемесячный Взнос',
        'rate': 'Годовая Процентная Ставка', 'period': 'Период', 'years': 'лет',
        'frequency': 'Частота Начисления', 'daily': 'Ежедневно', 'monthly_freq': 'Ежемесячно',
        'quarterly': 'Ежеквартально', 'annually': 'Ежегодно',
        'calculate': 'Рассчитать Рост 📊',
        'future_value': 'Будущая Стоимость', 'total_interest': 'Общий Процент',
        'total_deposits': 'Всего Вкладов', 'interest_earned': 'Заработанные Проценты',
        'growth': 'Рост со Временем', 'vs_simple': 'Сложные vs Простые Проценты',
        'simple': 'Простые Проценты', 'compound': 'Сложные Проценты',
        'extra': 'Вы зарабатываете {amount} больше со сложными процентами!',
        'what_is': 'Что такое Сложные Проценты?',
        'what_desc': 'Сложные проценты - это проценты, рассчитанные на начальный капитал и накопленные проценты за предыдущие периоды.'
    },
    'tr': {
        'lang': 'tr', 'locale': 'tr_TR', 'flag': '🇹🇷', 'name': 'Türkçe',
        'title': 'Bileşik Faiz Hesaplayıcı | Ücretsiz Yatırım Hesaplayıcı',
        'desc': 'Ücretsiz bileşik faiz hesaplayıcı. Yatırımlarınızın günlük, aylık veya yıllık bileşik faizle nasıl büyüdüğünü görün.',
        'h1': 'Bileşik Faiz <span class="text-emerald-400">Hesaplayıcı</span>',
        'subtitle': 'Paranızın zaman içinde nasıl büyüdüğünü görün',
        'enter_details': 'Bilgilerinizi Girin',
        'initial': 'Başlangıç Yatırımı', 'monthly': 'Aylık Katkı',
        'rate': 'Yıllık Faiz Oranı', 'period': 'Süre', 'years': 'yıl',
        'frequency': 'Bileşik Sıklığı', 'daily': 'Günlük', 'monthly_freq': 'Aylık',
        'quarterly': 'Üç Aylık', 'annually': 'Yıllık',
        'calculate': 'Büyümeyi Hesapla 📊',
        'future_value': 'Gelecek Değer', 'total_interest': 'Toplam Faiz',
        'total_deposits': 'Toplam Mevduat', 'interest_earned': 'Kazanılan Faiz',
        'growth': 'Zaman İçinde Büyüme', 'vs_simple': 'Bileşik vs Basit Faiz',
        'simple': 'Basit Faiz', 'compound': 'Bileşik Faiz',
        'extra': 'Bileşik faizle {amount} daha fazla kazanırsınız!',
        'what_is': 'Bileşik Faiz Nedir?',
        'what_desc': 'Bileşik faiz, ilk anapara ve önceki dönemlerden biriken faiz üzerinden hesaplanan faizdir.'
    },
}

# Language selector HTML
def get_lang_selector(current_lang):
    langs = [('en', '🇺🇸', '/'), ('de', '🇩🇪', '/de/'), ('es', '🇪🇸', '/es/'), ('fr', '🇫🇷', '/fr/'),
             ('pt', '🇧🇷', '/pt/'), ('zh', '🇨🇳', '/zh/'), ('ja', '🇯🇵', '/ja/'), ('hi', '🇮🇳', '/hi/'),
             ('ar', '🇸🇦', '/ar/'), ('ru', '🇷🇺', '/ru/'), ('tr', '🇹🇷', '/tr/')]
    current_flag = '🇺🇸' if current_lang == 'en' else [l[1] for l in langs if l[0] == current_lang][0]
    
    options = ''.join([f'<a href="{url}" class="block px-3 py-2 text-sm hover:bg-white/10">{flag}</a>' for lang, flag, url in langs])
    return f'''<div class="relative" id="langDropdownContainer">
        <button id="langDropdownBtn" class="text-white/70 hover:text-white text-lg md:text-2xl" onclick="event.stopPropagation(); document.getElementById('langDropdown').classList.toggle('hidden')">{current_flag}</button>
        <div id="langDropdown" class="hidden absolute right-0 mt-2 w-16 bg-slate-800/95 rounded-lg z-50 max-h-[70vh] overflow-y-auto">{options}</div>
    </div>'''

template = '''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://compoundcalc.org/{lang}/">
    <link rel="alternate" hreflang="en" href="https://compoundcalc.org/">
    <link rel="alternate" hreflang="{lang}" href="https://compoundcalc.org/{lang}/">
    <link rel="alternate" hreflang="x-default" href="https://compoundcalc.org/">
    <meta property="og:title" content="{title}">
    <meta property="og:url" content="https://compoundcalc.org/{lang}/">
    <meta property="og:locale" content="{locale}">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E📈%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .input-field {{ background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }}
        .input-field:focus {{ border-color: #10b981; outline: none; box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2); }}
        .btn-primary {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); }}
        .btn-primary:hover {{ background: linear-gradient(135deg, #059669 0%, #047857 100%); }}
        .result-card {{ background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.05) 100%); }}
    </style>
</head>
<body class="text-white">
    <header class="py-6 px-4">
        <div class="max-w-5xl mx-auto flex items-center justify-between">
            <a href="/{lang}/" class="flex items-center gap-3">
                <span class="text-3xl">📈</span>
                <span class="text-xl font-bold">Compound<span class="text-emerald-400">Calc</span></span>
            </a>
            <div class="flex items-center gap-4">
                <select id="currency" class="bg-transparent border border-white/20 rounded-lg px-3 py-1 text-sm">
                    <option value="$">$ USD</option><option value="€">€ EUR</option><option value="£">£ GBP</option>
                    <option value="¥">¥ JPY</option><option value="₹">₹ INR</option>
                </select>
                {lang_selector}
            </div>
        </div>
    </header>
    <main class="px-4 pb-12">
        <div class="max-w-5xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl md:text-4xl font-bold mb-3">{h1}</h1>
                <p class="text-white/60 text-lg">{subtitle}</p>
            </div>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="glass rounded-2xl p-6">
                    <h2 class="text-xl font-semibold mb-6 flex items-center gap-2"><span>🧮</span> {enter_details}</h2>
                    <div class="space-y-5">
                        <div><label class="block text-sm text-white/70 mb-2">{initial}</label>
                            <div class="relative"><span id="currencySymbol" class="absolute left-4 top-1/2 -translate-y-1/2 text-white/50">$</span>
                            <input type="number" id="principal" value="10000" min="0" step="100" class="input-field w-full rounded-xl py-3 pl-10 pr-4 text-lg font-medium"></div></div>
                        <div><label class="block text-sm text-white/70 mb-2">{monthly}</label>
                            <div class="relative"><span class="absolute left-4 top-1/2 -translate-y-1/2 text-white/50">$</span>
                            <input type="number" id="monthly" value="500" min="0" step="50" class="input-field w-full rounded-xl py-3 pl-10 pr-4 text-lg font-medium"></div></div>
                        <div><label class="block text-sm text-white/70 mb-2">{rate}</label>
                            <div class="relative"><input type="number" id="rate" value="7" min="0" max="100" step="0.1" class="input-field w-full rounded-xl py-3 px-4 pr-10 text-lg font-medium">
                            <span class="absolute right-4 top-1/2 -translate-y-1/2 text-white/50">%</span></div></div>
                        <div><label class="block text-sm text-white/70 mb-2">{period}</label>
                            <div class="relative"><input type="number" id="years" value="20" min="1" max="100" class="input-field w-full rounded-xl py-3 px-4 pr-16 text-lg font-medium">
                            <span class="absolute right-4 top-1/2 -translate-y-1/2 text-white/50">{years}</span></div></div>
                        <div><label class="block text-sm text-white/70 mb-2">{frequency}</label>
                            <select id="frequency" class="input-field w-full rounded-xl py-3 px-4 text-lg">
                                <option value="365">{daily}</option><option value="12" selected>{monthly_freq}</option>
                                <option value="4">{quarterly}</option><option value="1">{annually}</option></select></div>
                        <button onclick="calculate()" class="btn-primary w-full py-4 rounded-xl text-lg font-semibold transition-all hover:scale-[1.02]">{calculate}</button>
                    </div>
                </div>
                <div class="space-y-6">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="result-card glass rounded-2xl p-5 text-center"><p class="text-white/60 text-sm mb-1">{future_value}</p><p id="futureValue" class="text-2xl md:text-3xl font-bold text-emerald-400">$260,464</p></div>
                        <div class="glass rounded-2xl p-5 text-center"><p class="text-white/60 text-sm mb-1">{total_interest}</p><p id="totalInterest" class="text-2xl md:text-3xl font-bold text-amber-400">$130,464</p></div>
                        <div class="glass rounded-2xl p-5 text-center"><p class="text-white/60 text-sm mb-1">{total_deposits}</p><p id="totalDeposits" class="text-xl md:text-2xl font-bold">$130,000</p></div>
                        <div class="glass rounded-2xl p-5 text-center"><p class="text-white/60 text-sm mb-1">{interest_earned}</p><p id="interestPercent" class="text-xl md:text-2xl font-bold text-emerald-400">100%</p></div>
                    </div>
                    <div class="glass rounded-2xl p-5"><h3 class="text-lg font-semibold mb-4">{growth}</h3><div class="h-64"><canvas id="growthChart"></canvas></div></div>
                    <div class="glass rounded-2xl p-5"><h3 class="text-lg font-semibold mb-3">{vs_simple}</h3>
                        <div class="flex items-center gap-4"><div class="flex-1"><p class="text-white/60 text-sm">{simple}</p><p id="simpleInterest" class="text-xl font-bold text-white/80">$150,000</p></div>
                        <div class="text-emerald-400 text-2xl">→</div><div class="flex-1 text-right"><p class="text-white/60 text-sm">{compound}</p><p id="compoundValue" class="text-xl font-bold text-emerald-400">$260,464</p></div></div>
                        <p id="extraEarned" class="text-center text-emerald-400 mt-3 text-sm">{extra}</p></div>
                </div>
            </div>
            <div class="mt-12 glass rounded-2xl p-6 md:p-8">
                <h2 class="text-2xl font-bold mb-4">{what_is}</h2>
                <p class="text-white/70 mb-4">{what_desc}</p>
                <div class="bg-slate-800/50 rounded-xl p-4 font-mono text-center">A = P(1 + r/n)<sup>nt</sup></div>
            </div>
        </div>
    </main>
    <footer class="py-8 px-4 border-t border-white/10"><div class="max-w-5xl mx-auto text-center text-white/40 text-sm"><p>© 2026 CompoundCalc</p></div></footer>
    <script>
        let chart = null;
        function formatCurrency(value) {{ const c = document.getElementById('currency').value; return c + value.toLocaleString('en-US', {{ maximumFractionDigits: 0 }}); }}
        function calculate() {{
            const P = parseFloat(document.getElementById('principal').value) || 0;
            const PMT = parseFloat(document.getElementById('monthly').value) || 0;
            const r = (parseFloat(document.getElementById('rate').value) || 0) / 100;
            const t = parseInt(document.getElementById('years').value) || 1;
            const n = parseInt(document.getElementById('frequency').value) || 12;
            const FV_principal = P * Math.pow(1 + r/n, n*t);
            let FV_contributions = 0;
            if (PMT > 0 && r > 0) {{ const mr = r / 12; const tm = t * 12; FV_contributions = PMT * ((Math.pow(1 + mr, tm) - 1) / mr); }}
            else if (PMT > 0) {{ FV_contributions = PMT * t * 12; }}
            const totalFV = FV_principal + FV_contributions;
            const totalDep = P + (PMT * t * 12);
            const totalInt = totalFV - totalDep;
            const intPct = totalDep > 0 ? (totalInt / totalDep * 100) : 0;
            const simple = P + (P * r * t) + (PMT * t * 12);
            document.getElementById('futureValue').textContent = formatCurrency(totalFV);
            document.getElementById('totalInterest').textContent = formatCurrency(totalInt);
            document.getElementById('totalDeposits').textContent = formatCurrency(totalDep);
            document.getElementById('interestPercent').textContent = intPct.toFixed(0) + '%';
            document.getElementById('simpleInterest').textContent = formatCurrency(simple);
            document.getElementById('compoundValue').textContent = formatCurrency(totalFV);
            document.getElementById('extraEarned').textContent = '{extra}'.replace('{{amount}}', formatCurrency(totalFV - simple));
            updateChart(P, PMT, r, t, n);
        }}
        function updateChart(P, PMT, r, t, n) {{
            const labels = [], compoundData = [], depositData = [];
            for (let y = 0; y <= t; y++) {{
                labels.push('Year ' + y);
                const fvp = P * Math.pow(1 + r/n, n*y);
                let fvc = 0;
                if (PMT > 0 && r > 0) {{ const mr = r / 12; fvc = PMT * ((Math.pow(1 + mr, y*12) - 1) / mr); }}
                else if (PMT > 0) {{ fvc = PMT * y * 12; }}
                compoundData.push(fvp + fvc); depositData.push(P + (PMT * y * 12));
            }}
            const ctx = document.getElementById('growthChart').getContext('2d');
            if (chart) chart.destroy();
            chart = new Chart(ctx, {{
                type: 'line', data: {{ labels, datasets: [
                    {{ label: 'Total', data: compoundData, borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.1)', fill: true, tension: 0.4 }},
                    {{ label: 'Deposits', data: depositData, borderColor: '#6b7280', borderDash: [5,5], fill: false }}
                ]}},
                options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ labels: {{ color: 'rgba(255,255,255,0.7)' }} }} }},
                    scales: {{ x: {{ ticks: {{ color: 'rgba(255,255,255,0.5)' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
                        y: {{ ticks: {{ color: 'rgba(255,255,255,0.5)', callback: v => '$'+(v/1000).toFixed(0)+'k' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }} }} }}
            }});
        }}
        document.getElementById('currency').addEventListener('change', function() {{ document.getElementById('currencySymbol').textContent = this.value; calculate(); }});
        document.querySelectorAll('input, select').forEach(el => el.addEventListener('input', calculate));
        document.addEventListener('click', () => document.getElementById('langDropdown').classList.add('hidden'));
        calculate();
    </script>
</body>
</html>'''

for lang, t in translations.items():
    dir_attr = ' dir="rtl"' if t.get('rtl') else ''
    lang_selector = get_lang_selector(lang)
    html = template.format(
        lang=lang, dir_attr=dir_attr, locale=t['locale'], lang_selector=lang_selector,
        title=t['title'], desc=t['desc'], h1=t['h1'], subtitle=t['subtitle'],
        enter_details=t['enter_details'], initial=t['initial'], monthly=t['monthly'],
        rate=t['rate'], period=t['period'], years=t['years'], frequency=t['frequency'],
        daily=t['daily'], monthly_freq=t['monthly_freq'], quarterly=t['quarterly'],
        annually=t['annually'], calculate=t['calculate'], future_value=t['future_value'],
        total_interest=t['total_interest'], total_deposits=t['total_deposits'],
        interest_earned=t['interest_earned'], growth=t['growth'], vs_simple=t['vs_simple'],
        simple=t['simple'], compound=t['compound'], extra=t['extra'],
        what_is=t['what_is'], what_desc=t['what_desc']
    )
    os.makedirs(lang, exist_ok=True)
    with open(f'{lang}/index.html', 'w') as f:
        f.write(html)
    print(f'Created: {lang}/index.html')

print('Done!')
