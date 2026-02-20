#!/usr/bin/env python3
"""Generate SEO articles for CompoundCalc.ai in 11 languages."""

import os

LANGUAGES = {
    'en': {'name': 'English', 'dir': '', 'flag': '🇺🇸'},
    'de': {'name': 'Deutsch', 'dir': 'de', 'flag': '🇩🇪'},
    'es': {'name': 'Español', 'dir': 'es', 'flag': '🇪🇸'},
    'fr': {'name': 'Français', 'dir': 'fr', 'flag': '🇫🇷'},
    'pt': {'name': 'Português', 'dir': 'pt', 'flag': '🇧🇷'},
    'zh': {'name': '中文', 'dir': 'zh', 'flag': '🇨🇳'},
    'ja': {'name': '日本語', 'dir': 'ja', 'flag': '🇯🇵'},
    'ru': {'name': 'Русский', 'dir': 'ru', 'flag': '🇷🇺'},
    'hi': {'name': 'हिन्दी', 'dir': 'hi', 'flag': '🇮🇳'},
    'ar': {'name': 'العربية', 'dir': 'ar', 'flag': '🇸🇦'},
    'tr': {'name': 'Türkçe', 'dir': 'tr', 'flag': '🇹🇷'},
}

# Article 1: Compound vs Simple Interest
COMPOUND_VS_SIMPLE = {
    'en': {
        'title': 'Compound Interest vs Simple Interest: What\'s the Difference?',
        'meta': 'Learn the key differences between compound and simple interest. See examples, formulas, and when each type benefits you most.',
        'h1': 'Compound Interest vs Simple Interest',
        'subtitle': 'Understanding the two types of interest and how they affect your money',
        'intro': 'When it comes to growing your money or understanding loan costs, the type of interest makes a <strong>huge difference</strong>. Let\'s break down compound vs simple interest in plain terms.',
        'what_simple_title': 'What is Simple Interest?',
        'what_simple': 'Simple interest is calculated only on the <strong>original principal</strong> (your initial deposit or loan amount). It doesn\'t change over time.',
        'simple_formula': 'Simple Interest = Principal × Rate × Time',
        'simple_example_title': 'Example:',
        'simple_example': 'You invest $1,000 at 5% simple interest for 3 years:<br>Interest = $1,000 × 0.05 × 3 = <strong>$150</strong><br>Total after 3 years: <strong>$1,150</strong>',
        'what_compound_title': 'What is Compound Interest?',
        'what_compound': 'Compound interest is calculated on the principal <strong>plus any accumulated interest</strong>. Your interest earns interest — this is what makes it so powerful.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Where: A = final amount, P = principal, r = rate, n = compounds per year, t = years',
        'compound_example_title': 'Same Example with Compound Interest:',
        'compound_example': 'You invest $1,000 at 5% compounded annually for 3 years:<br>Year 1: $1,000 × 1.05 = $1,050<br>Year 2: $1,050 × 1.05 = $1,102.50<br>Year 3: $1,102.50 × 1.05 = <strong>$1,157.63</strong>',
        'difference_title': 'The Difference: $7.63 Extra',
        'difference': 'With compound interest, you earned <strong>$157.63</strong> vs <strong>$150</strong> with simple interest. That\'s 5% more earnings! And this gap grows dramatically over longer periods.',
        'table_title': 'Comparison Over Time ($10,000 at 7%)',
        'table_years': 'Years',
        'table_simple': 'Simple Interest',
        'table_compound': 'Compound Interest',
        'table_diff': 'Difference',
        'when_title': 'When Each Type is Used',
        'when_simple_title': 'Simple Interest is common in:',
        'when_simple_list': ['Car loans', 'Short-term personal loans', 'Some bonds', 'Interest-only mortgages'],
        'when_compound_title': 'Compound Interest is common in:',
        'when_compound_list': ['Savings accounts', 'Investment accounts', 'Credit cards (works against you!)', 'Mortgages', 'Student loans'],
        'key_title': 'Key Takeaways',
        'key_1': '<strong>For savings:</strong> You want compound interest — the more frequent the compounding, the better',
        'key_2': '<strong>For loans:</strong> Simple interest costs you less over time',
        'key_3': '<strong>Time matters:</strong> Compound interest benefits grow exponentially with time',
        'key_4': '<strong>Start early:</strong> The earlier you start investing with compound interest, the more dramatic the results',
        'cta_title': 'Calculate Your Growth',
        'cta_text': 'Use our free compound interest calculator to see how your money can grow over time.',
        'cta_button': 'Open Calculator →',
        'back': '← Calculator',
    },
    'de': {
        'title': 'Zinseszins vs Einfacher Zins: Was ist der Unterschied?',
        'meta': 'Lernen Sie die wichtigsten Unterschiede zwischen Zinseszins und einfachem Zins. Mit Beispielen, Formeln und wann welche Art am besten für Sie ist.',
        'h1': 'Zinseszins vs Einfacher Zins',
        'subtitle': 'Die zwei Zinsarten verstehen und wie sie Ihr Geld beeinflussen',
        'intro': 'Wenn es darum geht, Ihr Geld zu vermehren oder Kreditkosten zu verstehen, macht die Zinsart einen <strong>großen Unterschied</strong>. Lassen Sie uns Zinseszins vs einfachen Zins verständlich erklären.',
        'what_simple_title': 'Was ist Einfacher Zins?',
        'what_simple': 'Einfacher Zins wird nur auf das <strong>ursprüngliche Kapital</strong> (Ihre anfängliche Einlage oder Kreditsumme) berechnet. Er ändert sich nicht über die Zeit.',
        'simple_formula': 'Einfacher Zins = Kapital × Zinssatz × Zeit',
        'simple_example_title': 'Beispiel:',
        'simple_example': 'Sie investieren 1.000 € zu 5% einfachem Zins für 3 Jahre:<br>Zinsen = 1.000 € × 0,05 × 3 = <strong>150 €</strong><br>Gesamt nach 3 Jahren: <strong>1.150 €</strong>',
        'what_compound_title': 'Was ist Zinseszins?',
        'what_compound': 'Zinseszins wird auf das Kapital <strong>plus alle aufgelaufenen Zinsen</strong> berechnet. Ihre Zinsen verdienen Zinsen — das macht ihn so mächtig.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Wobei: A = Endbetrag, P = Kapital, r = Zinssatz, n = Zinsperioden pro Jahr, t = Jahre',
        'compound_example_title': 'Gleiches Beispiel mit Zinseszins:',
        'compound_example': 'Sie investieren 1.000 € zu 5% jährlich verzinst für 3 Jahre:<br>Jahr 1: 1.000 € × 1,05 = 1.050 €<br>Jahr 2: 1.050 € × 1,05 = 1.102,50 €<br>Jahr 3: 1.102,50 € × 1,05 = <strong>1.157,63 €</strong>',
        'difference_title': 'Der Unterschied: 7,63 € mehr',
        'difference': 'Mit Zinseszins haben Sie <strong>157,63 €</strong> verdient vs <strong>150 €</strong> mit einfachem Zins. Das sind 5% mehr Ertrag! Und dieser Unterschied wächst dramatisch über längere Zeiträume.',
        'table_title': 'Vergleich über Zeit (10.000 € bei 7%)',
        'table_years': 'Jahre',
        'table_simple': 'Einfacher Zins',
        'table_compound': 'Zinseszins',
        'table_diff': 'Unterschied',
        'when_title': 'Wann wird welche Art verwendet?',
        'when_simple_title': 'Einfacher Zins ist üblich bei:',
        'when_simple_list': ['Autokrediten', 'Kurzfristigen Privatkrediten', 'Einigen Anleihen', 'Endfälligen Hypotheken'],
        'when_compound_title': 'Zinseszins ist üblich bei:',
        'when_compound_list': ['Sparkonten', 'Anlagekonten', 'Kreditkarten (wirkt gegen Sie!)', 'Hypotheken', 'Studienkrediten'],
        'key_title': 'Wichtige Erkenntnisse',
        'key_1': '<strong>Beim Sparen:</strong> Sie wollen Zinseszins — je häufiger die Verzinsung, desto besser',
        'key_2': '<strong>Bei Krediten:</strong> Einfacher Zins kostet Sie weniger über die Zeit',
        'key_3': '<strong>Zeit ist wichtig:</strong> Zinseszins-Vorteile wachsen exponentiell mit der Zeit',
        'key_4': '<strong>Früh anfangen:</strong> Je früher Sie mit Zinseszins investieren, desto dramatischer die Ergebnisse',
        'cta_title': 'Berechnen Sie Ihr Wachstum',
        'cta_text': 'Nutzen Sie unseren kostenlosen Zinseszinsrechner um zu sehen, wie Ihr Geld über die Zeit wachsen kann.',
        'cta_button': 'Rechner öffnen →',
        'back': '← Rechner',
    },
    'es': {
        'title': 'Interés Compuesto vs Interés Simple: ¿Cuál es la Diferencia?',
        'meta': 'Aprende las diferencias clave entre el interés compuesto y simple. Ve ejemplos, fórmulas y cuándo cada tipo te beneficia más.',
        'h1': 'Interés Compuesto vs Interés Simple',
        'subtitle': 'Entendiendo los dos tipos de interés y cómo afectan tu dinero',
        'intro': 'Cuando se trata de hacer crecer tu dinero o entender los costos de préstamos, el tipo de interés hace una <strong>gran diferencia</strong>. Vamos a explicar interés compuesto vs simple en términos claros.',
        'what_simple_title': '¿Qué es el Interés Simple?',
        'what_simple': 'El interés simple se calcula solo sobre el <strong>capital original</strong> (tu depósito inicial o monto del préstamo). No cambia con el tiempo.',
        'simple_formula': 'Interés Simple = Capital × Tasa × Tiempo',
        'simple_example_title': 'Ejemplo:',
        'simple_example': 'Inviertes $1,000 al 5% de interés simple por 3 años:<br>Interés = $1,000 × 0.05 × 3 = <strong>$150</strong><br>Total después de 3 años: <strong>$1,150</strong>',
        'what_compound_title': '¿Qué es el Interés Compuesto?',
        'what_compound': 'El interés compuesto se calcula sobre el capital <strong>más cualquier interés acumulado</strong>. Tu interés gana interés — esto es lo que lo hace tan poderoso.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Donde: A = monto final, P = capital, r = tasa, n = capitalizaciones por año, t = años',
        'compound_example_title': 'Mismo Ejemplo con Interés Compuesto:',
        'compound_example': 'Inviertes $1,000 al 5% compuesto anualmente por 3 años:<br>Año 1: $1,000 × 1.05 = $1,050<br>Año 2: $1,050 × 1.05 = $1,102.50<br>Año 3: $1,102.50 × 1.05 = <strong>$1,157.63</strong>',
        'difference_title': 'La Diferencia: $7.63 Extra',
        'difference': 'Con interés compuesto, ganaste <strong>$157.63</strong> vs <strong>$150</strong> con interés simple. ¡Eso es 5% más de ganancias! Y esta brecha crece dramáticamente en períodos más largos.',
        'table_title': 'Comparación en el Tiempo ($10,000 al 7%)',
        'table_years': 'Años',
        'table_simple': 'Interés Simple',
        'table_compound': 'Interés Compuesto',
        'table_diff': 'Diferencia',
        'when_title': 'Cuándo se Usa Cada Tipo',
        'when_simple_title': 'El interés simple es común en:',
        'when_simple_list': ['Préstamos de auto', 'Préstamos personales a corto plazo', 'Algunos bonos', 'Hipotecas de solo interés'],
        'when_compound_title': 'El interés compuesto es común en:',
        'when_compound_list': ['Cuentas de ahorro', 'Cuentas de inversión', 'Tarjetas de crédito (¡trabaja en tu contra!)', 'Hipotecas', 'Préstamos estudiantiles'],
        'key_title': 'Puntos Clave',
        'key_1': '<strong>Para ahorrar:</strong> Quieres interés compuesto — mientras más frecuente la capitalización, mejor',
        'key_2': '<strong>Para préstamos:</strong> El interés simple te cuesta menos a largo plazo',
        'key_3': '<strong>El tiempo importa:</strong> Los beneficios del interés compuesto crecen exponencialmente con el tiempo',
        'key_4': '<strong>Empieza temprano:</strong> Mientras más temprano empieces a invertir con interés compuesto, más dramáticos los resultados',
        'cta_title': 'Calcula Tu Crecimiento',
        'cta_text': 'Usa nuestra calculadora gratuita de interés compuesto para ver cómo puede crecer tu dinero.',
        'cta_button': 'Abrir Calculadora →',
        'back': '← Calculadora',
    },
    'fr': {
        'title': 'Intérêts Composés vs Intérêts Simples: Quelle Différence?',
        'meta': 'Découvrez les différences clés entre les intérêts composés et simples. Exemples, formules et quand chaque type vous avantage le plus.',
        'h1': 'Intérêts Composés vs Intérêts Simples',
        'subtitle': 'Comprendre les deux types d\'intérêts et leur impact sur votre argent',
        'intro': 'Quand il s\'agit de faire fructifier votre argent ou de comprendre les coûts d\'emprunt, le type d\'intérêt fait une <strong>énorme différence</strong>. Expliquons les intérêts composés vs simples en termes clairs.',
        'what_simple_title': 'Qu\'est-ce que l\'Intérêt Simple?',
        'what_simple': 'L\'intérêt simple est calculé uniquement sur le <strong>capital initial</strong> (votre dépôt initial ou montant du prêt). Il ne change pas dans le temps.',
        'simple_formula': 'Intérêt Simple = Capital × Taux × Temps',
        'simple_example_title': 'Exemple:',
        'simple_example': 'Vous investissez 1 000 € à 5% d\'intérêt simple pendant 3 ans:<br>Intérêt = 1 000 € × 0,05 × 3 = <strong>150 €</strong><br>Total après 3 ans: <strong>1 150 €</strong>',
        'what_compound_title': 'Qu\'est-ce que l\'Intérêt Composé?',
        'what_compound': 'L\'intérêt composé est calculé sur le capital <strong>plus les intérêts accumulés</strong>. Vos intérêts génèrent des intérêts — c\'est ce qui le rend si puissant.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Où: A = montant final, P = capital, r = taux, n = compositions par an, t = années',
        'compound_example_title': 'Même Exemple avec Intérêt Composé:',
        'compound_example': 'Vous investissez 1 000 € à 5% composé annuellement pendant 3 ans:<br>Année 1: 1 000 € × 1,05 = 1 050 €<br>Année 2: 1 050 € × 1,05 = 1 102,50 €<br>Année 3: 1 102,50 € × 1,05 = <strong>1 157,63 €</strong>',
        'difference_title': 'La Différence: 7,63 € de Plus',
        'difference': 'Avec les intérêts composés, vous avez gagné <strong>157,63 €</strong> contre <strong>150 €</strong> avec l\'intérêt simple. C\'est 5% de gains en plus! Et cet écart croît dramatiquement sur de longues périodes.',
        'table_title': 'Comparaison dans le Temps (10 000 € à 7%)',
        'table_years': 'Années',
        'table_simple': 'Intérêt Simple',
        'table_compound': 'Intérêt Composé',
        'table_diff': 'Différence',
        'when_title': 'Quand Chaque Type est Utilisé',
        'when_simple_title': 'L\'intérêt simple est courant pour:',
        'when_simple_list': ['Prêts auto', 'Prêts personnels court terme', 'Certaines obligations', 'Prêts hypothécaires in fine'],
        'when_compound_title': 'L\'intérêt composé est courant pour:',
        'when_compound_list': ['Comptes d\'épargne', 'Comptes d\'investissement', 'Cartes de crédit (joue contre vous!)', 'Hypothèques', 'Prêts étudiants'],
        'key_title': 'Points Clés',
        'key_1': '<strong>Pour l\'épargne:</strong> Vous voulez l\'intérêt composé — plus la composition est fréquente, mieux c\'est',
        'key_2': '<strong>Pour les prêts:</strong> L\'intérêt simple vous coûte moins sur la durée',
        'key_3': '<strong>Le temps compte:</strong> Les avantages des intérêts composés croissent exponentiellement avec le temps',
        'key_4': '<strong>Commencez tôt:</strong> Plus vous commencez tôt à investir avec intérêts composés, plus les résultats sont spectaculaires',
        'cta_title': 'Calculez Votre Croissance',
        'cta_text': 'Utilisez notre calculateur d\'intérêts composés gratuit pour voir comment votre argent peut croître.',
        'cta_button': 'Ouvrir le Calculateur →',
        'back': '← Calculateur',
    },
    'pt': {
        'title': 'Juros Compostos vs Juros Simples: Qual a Diferença?',
        'meta': 'Aprenda as principais diferenças entre juros compostos e simples. Veja exemplos, fórmulas e quando cada tipo mais te beneficia.',
        'h1': 'Juros Compostos vs Juros Simples',
        'subtitle': 'Entendendo os dois tipos de juros e como afetam seu dinheiro',
        'intro': 'Quando se trata de fazer seu dinheiro crescer ou entender custos de empréstimos, o tipo de juros faz uma <strong>enorme diferença</strong>. Vamos explicar juros compostos vs simples em termos claros.',
        'what_simple_title': 'O que são Juros Simples?',
        'what_simple': 'Juros simples são calculados apenas sobre o <strong>capital original</strong> (seu depósito inicial ou valor do empréstimo). Não muda ao longo do tempo.',
        'simple_formula': 'Juros Simples = Capital × Taxa × Tempo',
        'simple_example_title': 'Exemplo:',
        'simple_example': 'Você investe R$1.000 a 5% de juros simples por 3 anos:<br>Juros = R$1.000 × 0,05 × 3 = <strong>R$150</strong><br>Total após 3 anos: <strong>R$1.150</strong>',
        'what_compound_title': 'O que são Juros Compostos?',
        'what_compound': 'Juros compostos são calculados sobre o capital <strong>mais quaisquer juros acumulados</strong>. Seus juros rendem juros — isso é o que os torna tão poderosos.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Onde: A = montante final, P = capital, r = taxa, n = composições por ano, t = anos',
        'compound_example_title': 'Mesmo Exemplo com Juros Compostos:',
        'compound_example': 'Você investe R$1.000 a 5% compostos anualmente por 3 anos:<br>Ano 1: R$1.000 × 1,05 = R$1.050<br>Ano 2: R$1.050 × 1,05 = R$1.102,50<br>Ano 3: R$1.102,50 × 1,05 = <strong>R$1.157,63</strong>',
        'difference_title': 'A Diferença: R$7,63 a Mais',
        'difference': 'Com juros compostos, você ganhou <strong>R$157,63</strong> vs <strong>R$150</strong> com juros simples. São 5% a mais de ganhos! E essa diferença cresce dramaticamente em períodos mais longos.',
        'table_title': 'Comparação ao Longo do Tempo (R$10.000 a 7%)',
        'table_years': 'Anos',
        'table_simple': 'Juros Simples',
        'table_compound': 'Juros Compostos',
        'table_diff': 'Diferença',
        'when_title': 'Quando Cada Tipo é Usado',
        'when_simple_title': 'Juros simples são comuns em:',
        'when_simple_list': ['Financiamentos de veículos', 'Empréstimos pessoais de curto prazo', 'Alguns títulos', 'Financiamentos com carência'],
        'when_compound_title': 'Juros compostos são comuns em:',
        'when_compound_list': ['Contas poupança', 'Contas de investimento', 'Cartões de crédito (trabalha contra você!)', 'Financiamentos imobiliários', 'Empréstimos estudantis'],
        'key_title': 'Pontos-Chave',
        'key_1': '<strong>Para poupar:</strong> Você quer juros compostos — quanto mais frequente a composição, melhor',
        'key_2': '<strong>Para empréstimos:</strong> Juros simples custam menos ao longo do tempo',
        'key_3': '<strong>O tempo importa:</strong> Os benefícios dos juros compostos crescem exponencialmente com o tempo',
        'key_4': '<strong>Comece cedo:</strong> Quanto mais cedo você começar a investir com juros compostos, mais dramáticos os resultados',
        'cta_title': 'Calcule Seu Crescimento',
        'cta_text': 'Use nossa calculadora gratuita de juros compostos para ver como seu dinheiro pode crescer.',
        'cta_button': 'Abrir Calculadora →',
        'back': '← Calculadora',
    },
    'zh': {
        'title': '复利与单利：有什么区别？',
        'meta': '了解复利和单利之间的主要区别。查看示例、公式，以及何时每种类型对您最有利。',
        'h1': '复利与单利',
        'subtitle': '理解两种利息类型及其对您资金的影响',
        'intro': '无论是增加您的资金还是了解贷款成本，利息类型都会产生<strong>巨大差异</strong>。让我们用简单的语言解释复利与单利。',
        'what_simple_title': '什么是单利？',
        'what_simple': '单利仅根据<strong>原始本金</strong>（您的初始存款或贷款金额）计算。它不会随时间变化。',
        'simple_formula': '单利 = 本金 × 利率 × 时间',
        'simple_example_title': '示例：',
        'simple_example': '您以5%单利投资1,000美元，期限3年：<br>利息 = 1,000美元 × 0.05 × 3 = <strong>150美元</strong><br>3年后总额：<strong>1,150美元</strong>',
        'what_compound_title': '什么是复利？',
        'what_compound': '复利是根据本金<strong>加上任何累积利息</strong>计算的。您的利息产生利息——这就是它如此强大的原因。',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': '其中：A = 最终金额，P = 本金，r = 利率，n = 每年复利次数，t = 年数',
        'compound_example_title': '相同示例使用复利：',
        'compound_example': '您以5%年复利投资1,000美元，期限3年：<br>第1年：1,000美元 × 1.05 = 1,050美元<br>第2年：1,050美元 × 1.05 = 1,102.50美元<br>第3年：1,102.50美元 × 1.05 = <strong>1,157.63美元</strong>',
        'difference_title': '差异：多出7.63美元',
        'difference': '使用复利，您赚取了<strong>157.63美元</strong>，而单利只有<strong>150美元</strong>。这多出5%的收益！而且这个差距在更长的时期内会急剧增长。',
        'table_title': '时间对比（10,000美元，7%利率）',
        'table_years': '年数',
        'table_simple': '单利',
        'table_compound': '复利',
        'table_diff': '差异',
        'when_title': '何时使用各种类型',
        'when_simple_title': '单利常见于：',
        'when_simple_list': ['汽车贷款', '短期个人贷款', '某些债券', '只付利息的抵押贷款'],
        'when_compound_title': '复利常见于：',
        'when_compound_list': ['储蓄账户', '投资账户', '信用卡（对您不利！）', '抵押贷款', '学生贷款'],
        'key_title': '关键要点',
        'key_1': '<strong>对于储蓄：</strong>您需要复利——复利频率越高越好',
        'key_2': '<strong>对于贷款：</strong>单利长期成本更低',
        'key_3': '<strong>时间很重要：</strong>复利的优势随时间呈指数增长',
        'key_4': '<strong>尽早开始：</strong>越早开始复利投资，效果越显著',
        'cta_title': '计算您的增长',
        'cta_text': '使用我们的免费复利计算器，查看您的资金如何随时间增长。',
        'cta_button': '打开计算器 →',
        'back': '← 计算器',
    },
    'ja': {
        'title': '複利と単利：その違いとは？',
        'meta': '複利と単利の主な違いを学びましょう。例、公式、そしてそれぞれがいつ最も有利かを確認できます。',
        'h1': '複利と単利の違い',
        'subtitle': '2種類の利息とお金への影響を理解する',
        'intro': 'お金を増やすにも、ローンのコストを理解するにも、利息の種類は<strong>大きな違い</strong>を生みます。複利と単利をわかりやすく解説します。',
        'what_simple_title': '単利とは？',
        'what_simple': '単利は<strong>元本</strong>（最初の預金またはローン金額）のみに基づいて計算されます。時間が経っても変わりません。',
        'simple_formula': '単利 = 元本 × 利率 × 期間',
        'simple_example_title': '例：',
        'simple_example': '年利5%の単利で10万円を3年間投資：<br>利息 = 10万円 × 0.05 × 3 = <strong>1.5万円</strong><br>3年後の合計：<strong>11.5万円</strong>',
        'what_compound_title': '複利とは？',
        'what_compound': '複利は元本<strong>と蓄積された利息</strong>に基づいて計算されます。利息が利息を生む — これが複利の力です。',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'A = 最終金額、P = 元本、r = 利率、n = 年間複利回数、t = 年数',
        'compound_example_title': '同じ例を複利で：',
        'compound_example': '年利5%の複利で10万円を3年間投資：<br>1年目：10万円 × 1.05 = 10.5万円<br>2年目：10.5万円 × 1.05 = 11.025万円<br>3年目：11.025万円 × 1.05 = <strong>11.576万円</strong>',
        'difference_title': '違い：763円の差',
        'difference': '複利では<strong>15,763円</strong>の利息、単利では<strong>15,000円</strong>。5%多く稼げます！この差は長期間になると劇的に大きくなります。',
        'table_title': '経時比較（100万円、年利7%）',
        'table_years': '年数',
        'table_simple': '単利',
        'table_compound': '複利',
        'table_diff': '差額',
        'when_title': 'それぞれの使用場面',
        'when_simple_title': '単利が一般的なもの：',
        'when_simple_list': ['自動車ローン', '短期個人ローン', '一部の債券', '利息のみの住宅ローン'],
        'when_compound_title': '複利が一般的なもの：',
        'when_compound_list': ['普通預金', '投資口座', 'クレジットカード（不利に働く！）', '住宅ローン', '学生ローン'],
        'key_title': '重要ポイント',
        'key_1': '<strong>貯蓄の場合：</strong>複利が欲しい — 複利の頻度が高いほど良い',
        'key_2': '<strong>ローンの場合：</strong>単利の方が長期的にコストが低い',
        'key_3': '<strong>時間が重要：</strong>複利のメリットは時間とともに指数関数的に成長',
        'key_4': '<strong>早く始める：</strong>複利投資を早く始めるほど、効果は劇的',
        'cta_title': '成長を計算',
        'cta_text': '無料の複利計算機で、お金がどのように成長するか確認しましょう。',
        'cta_button': '計算機を開く →',
        'back': '← 計算機',
    },
    'ru': {
        'title': 'Сложные проценты vs Простые: В чём разница?',
        'meta': 'Узнайте ключевые различия между сложными и простыми процентами. Примеры, формулы и когда каждый тип выгоднее.',
        'h1': 'Сложные проценты vs Простые',
        'subtitle': 'Понимание двух типов процентов и их влияния на ваши деньги',
        'intro': 'Когда речь идёт о приумножении денег или понимании стоимости кредита, тип процента имеет <strong>огромное значение</strong>. Разберём сложные vs простые проценты простым языком.',
        'what_simple_title': 'Что такое Простые Проценты?',
        'what_simple': 'Простые проценты рассчитываются только от <strong>первоначальной суммы</strong> (вашего начального вклада или суммы кредита). Они не меняются со временем.',
        'simple_formula': 'Простые Проценты = Сумма × Ставка × Время',
        'simple_example_title': 'Пример:',
        'simple_example': 'Вы инвестируете $1,000 под 5% простых на 3 года:<br>Проценты = $1,000 × 0.05 × 3 = <strong>$150</strong><br>Итого через 3 года: <strong>$1,150</strong>',
        'what_compound_title': 'Что такое Сложные Проценты?',
        'what_compound': 'Сложные проценты рассчитываются от суммы <strong>плюс накопленные проценты</strong>. Ваши проценты приносят проценты — вот что делает их такими мощными.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Где: A = итоговая сумма, P = начальная сумма, r = ставка, n = начислений в год, t = лет',
        'compound_example_title': 'Тот же пример со сложными процентами:',
        'compound_example': 'Вы инвестируете $1,000 под 5% годовых сложных на 3 года:<br>Год 1: $1,000 × 1.05 = $1,050<br>Год 2: $1,050 × 1.05 = $1,102.50<br>Год 3: $1,102.50 × 1.05 = <strong>$1,157.63</strong>',
        'difference_title': 'Разница: $7.63 дополнительно',
        'difference': 'Со сложными процентами вы заработали <strong>$157.63</strong> против <strong>$150</strong> с простыми. Это на 5% больше! И эта разница резко растёт на длительных периодах.',
        'table_title': 'Сравнение во времени ($10,000 под 7%)',
        'table_years': 'Лет',
        'table_simple': 'Простые',
        'table_compound': 'Сложные',
        'table_diff': 'Разница',
        'when_title': 'Когда используется каждый тип',
        'when_simple_title': 'Простые проценты типичны для:',
        'when_simple_list': ['Автокредитов', 'Краткосрочных займов', 'Некоторых облигаций', 'Процентных ипотек'],
        'when_compound_title': 'Сложные проценты типичны для:',
        'when_compound_list': ['Сберегательных счетов', 'Инвестиционных счетов', 'Кредитных карт (работают против вас!)', 'Ипотеки', 'Студенческих кредитов'],
        'key_title': 'Ключевые выводы',
        'key_1': '<strong>Для сбережений:</strong> Вам нужны сложные проценты — чем чаще начисление, тем лучше',
        'key_2': '<strong>Для кредитов:</strong> Простые проценты обходятся дешевле',
        'key_3': '<strong>Время важно:</strong> Преимущества сложных процентов растут экспоненциально',
        'key_4': '<strong>Начните рано:</strong> Чем раньше вы начнёте инвестировать со сложными процентами, тем впечатлительнее результат',
        'cta_title': 'Рассчитайте ваш рост',
        'cta_text': 'Используйте наш бесплатный калькулятор сложных процентов, чтобы увидеть, как могут расти ваши деньги.',
        'cta_button': 'Открыть калькулятор →',
        'back': '← Калькулятор',
    },
    'hi': {
        'title': 'चक्रवृद्धि ब्याज vs साधारण ब्याज: क्या अंतर है?',
        'meta': 'चक्रवृद्धि और साधारण ब्याज के बीच मुख्य अंतर जानें। उदाहरण, सूत्र और कब कौन सा प्रकार आपके लिए सबसे अच्छा है।',
        'h1': 'चक्रवृद्धि ब्याज vs साधारण ब्याज',
        'subtitle': 'दो प्रकार के ब्याज को समझें और वे आपके पैसे को कैसे प्रभावित करते हैं',
        'intro': 'जब आपके पैसे बढ़ाने या ऋण की लागत समझने की बात आती है, तो ब्याज का प्रकार <strong>बहुत बड़ा अंतर</strong> बनाता है। आइए चक्रवृद्धि vs साधारण ब्याज को सरल भाषा में समझें।',
        'what_simple_title': 'साधारण ब्याज क्या है?',
        'what_simple': 'साधारण ब्याज केवल <strong>मूल राशि</strong> (आपकी प्रारंभिक जमा या ऋण राशि) पर गणना की जाती है। यह समय के साथ नहीं बदलता।',
        'simple_formula': 'साधारण ब्याज = मूलधन × दर × समय',
        'simple_example_title': 'उदाहरण:',
        'simple_example': 'आप ₹1,000 को 5% साधारण ब्याज पर 3 साल के लिए निवेश करते हैं:<br>ब्याज = ₹1,000 × 0.05 × 3 = <strong>₹150</strong><br>3 साल बाद कुल: <strong>₹1,150</strong>',
        'what_compound_title': 'चक्रवृद्धि ब्याज क्या है?',
        'what_compound': 'चक्रवृद्धि ब्याज मूलधन <strong>और किसी भी संचित ब्याज</strong> पर गणना की जाती है। आपका ब्याज ब्याज कमाता है — यही इसे इतना शक्तिशाली बनाता है।',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'जहाँ: A = अंतिम राशि, P = मूलधन, r = दर, n = प्रति वर्ष चक्रवृद्धि, t = वर्ष',
        'compound_example_title': 'वही उदाहरण चक्रवृद्धि ब्याज के साथ:',
        'compound_example': 'आप ₹1,000 को 5% वार्षिक चक्रवृद्धि पर 3 साल के लिए निवेश करते हैं:<br>वर्ष 1: ₹1,000 × 1.05 = ₹1,050<br>वर्ष 2: ₹1,050 × 1.05 = ₹1,102.50<br>वर्ष 3: ₹1,102.50 × 1.05 = <strong>₹1,157.63</strong>',
        'difference_title': 'अंतर: ₹7.63 अतिरिक्त',
        'difference': 'चक्रवृद्धि ब्याज से आपने <strong>₹157.63</strong> कमाए vs साधारण ब्याज से <strong>₹150</strong>। यह 5% अधिक कमाई है! और यह अंतर लंबी अवधि में नाटकीय रूप से बढ़ता है।',
        'table_title': 'समय के साथ तुलना (₹10,000 पर 7%)',
        'table_years': 'वर्ष',
        'table_simple': 'साधारण ब्याज',
        'table_compound': 'चक्रवृद्धि ब्याज',
        'table_diff': 'अंतर',
        'when_title': 'प्रत्येक प्रकार कब उपयोग होता है',
        'when_simple_title': 'साधारण ब्याज आम है:',
        'when_simple_list': ['कार ऋण', 'अल्पकालिक व्यक्तिगत ऋण', 'कुछ बॉन्ड', 'केवल-ब्याज बंधक'],
        'when_compound_title': 'चक्रवृद्धि ब्याज आम है:',
        'when_compound_list': ['बचत खाते', 'निवेश खाते', 'क्रेडिट कार्ड (आपके खिलाफ काम करता है!)', 'बंधक', 'छात्र ऋण'],
        'key_title': 'मुख्य बिंदु',
        'key_1': '<strong>बचत के लिए:</strong> आप चक्रवृद्धि ब्याज चाहते हैं — जितनी बार चक्रवृद्धि, उतना बेहतर',
        'key_2': '<strong>ऋण के लिए:</strong> साधारण ब्याज समय के साथ कम खर्चीला है',
        'key_3': '<strong>समय मायने रखता है:</strong> चक्रवृद्धि ब्याज के लाभ समय के साथ घातीय रूप से बढ़ते हैं',
        'key_4': '<strong>जल्दी शुरू करें:</strong> आप जितनी जल्दी चक्रवृद्धि ब्याज के साथ निवेश शुरू करेंगे, परिणाम उतने नाटकीय होंगे',
        'cta_title': 'अपनी वृद्धि की गणना करें',
        'cta_text': 'हमारे मुफ्त चक्रवृद्धि ब्याज कैलकुलेटर का उपयोग करके देखें कि आपका पैसा कैसे बढ़ सकता है।',
        'cta_button': 'कैलकुलेटर खोलें →',
        'back': '← कैलकुलेटर',
    },
    'ar': {
        'title': 'الفائدة المركبة مقابل الفائدة البسيطة: ما الفرق؟',
        'meta': 'تعرف على الفروقات الرئيسية بين الفائدة المركبة والبسيطة. أمثلة، صيغ، ومتى يفيدك كل نوع أكثر.',
        'h1': 'الفائدة المركبة مقابل البسيطة',
        'subtitle': 'فهم نوعي الفائدة وكيف يؤثران على أموالك',
        'intro': 'عندما يتعلق الأمر بتنمية أموالك أو فهم تكاليف القروض، يُحدث نوع الفائدة <strong>فرقًا كبيرًا</strong>. دعنا نشرح الفائدة المركبة مقابل البسيطة بشكل واضح.',
        'what_simple_title': 'ما هي الفائدة البسيطة؟',
        'what_simple': 'تُحسب الفائدة البسيطة فقط على <strong>المبلغ الأصلي</strong> (إيداعك الأولي أو مبلغ القرض). لا تتغير بمرور الوقت.',
        'simple_formula': 'الفائدة البسيطة = رأس المال × المعدل × الوقت',
        'simple_example_title': 'مثال:',
        'simple_example': 'تستثمر 1,000$ بفائدة بسيطة 5% لمدة 3 سنوات:<br>الفائدة = 1,000$ × 0.05 × 3 = <strong>150$</strong><br>الإجمالي بعد 3 سنوات: <strong>1,150$</strong>',
        'what_compound_title': 'ما هي الفائدة المركبة؟',
        'what_compound': 'تُحسب الفائدة المركبة على رأس المال <strong>بالإضافة إلى أي فائدة متراكمة</strong>. فائدتك تكسب فائدة — هذا ما يجعلها قوية جدًا.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'حيث: A = المبلغ النهائي، P = رأس المال، r = المعدل، n = مرات التركيب سنويًا، t = السنوات',
        'compound_example_title': 'نفس المثال بالفائدة المركبة:',
        'compound_example': 'تستثمر 1,000$ بفائدة مركبة 5% سنويًا لمدة 3 سنوات:<br>السنة 1: 1,000$ × 1.05 = 1,050$<br>السنة 2: 1,050$ × 1.05 = 1,102.50$<br>السنة 3: 1,102.50$ × 1.05 = <strong>1,157.63$</strong>',
        'difference_title': 'الفرق: 7.63$ إضافية',
        'difference': 'بالفائدة المركبة، ربحت <strong>157.63$</strong> مقابل <strong>150$</strong> بالفائدة البسيطة. هذا 5% أرباح إضافية! وهذه الفجوة تنمو بشكل كبير على فترات أطول.',
        'table_title': 'مقارنة عبر الزمن (10,000$ بنسبة 7%)',
        'table_years': 'السنوات',
        'table_simple': 'فائدة بسيطة',
        'table_compound': 'فائدة مركبة',
        'table_diff': 'الفرق',
        'when_title': 'متى يُستخدم كل نوع',
        'when_simple_title': 'الفائدة البسيطة شائعة في:',
        'when_simple_list': ['قروض السيارات', 'القروض الشخصية قصيرة الأجل', 'بعض السندات', 'الرهون العقارية بالفائدة فقط'],
        'when_compound_title': 'الفائدة المركبة شائعة في:',
        'when_compound_list': ['حسابات التوفير', 'حسابات الاستثمار', 'بطاقات الائتمان (تعمل ضدك!)', 'الرهون العقارية', 'قروض الطلاب'],
        'key_title': 'النقاط الرئيسية',
        'key_1': '<strong>للادخار:</strong> تريد الفائدة المركبة — كلما زاد التركيب، كان أفضل',
        'key_2': '<strong>للقروض:</strong> الفائدة البسيطة تكلفك أقل على المدى الطويل',
        'key_3': '<strong>الوقت مهم:</strong> فوائد الفائدة المركبة تنمو أسيًا مع الوقت',
        'key_4': '<strong>ابدأ مبكرًا:</strong> كلما بدأت الاستثمار بالفائدة المركبة مبكرًا، كانت النتائج أكثر دراماتيكية',
        'cta_title': 'احسب نموك',
        'cta_text': 'استخدم حاسبة الفائدة المركبة المجانية لترى كيف يمكن أن تنمو أموالك.',
        'cta_button': 'افتح الحاسبة →',
        'back': '← الحاسبة',
    },
    'tr': {
        'title': 'Bileşik Faiz vs Basit Faiz: Fark Nedir?',
        'meta': 'Bileşik ve basit faiz arasındaki temel farkları öğrenin. Örnekler, formüller ve her türün ne zaman daha avantajlı olduğunu görün.',
        'h1': 'Bileşik Faiz vs Basit Faiz',
        'subtitle': 'İki faiz türünü ve paranızı nasıl etkilediğini anlama',
        'intro': 'Paranızı büyütmek veya kredi maliyetlerini anlamak söz konusu olduğunda, faiz türü <strong>büyük fark</strong> yaratır. Bileşik vs basit faizi basit terimlerle açıklayalım.',
        'what_simple_title': 'Basit Faiz Nedir?',
        'what_simple': 'Basit faiz yalnızca <strong>orijinal anapara</strong> (ilk yatırımınız veya kredi tutarı) üzerinden hesaplanır. Zamanla değişmez.',
        'simple_formula': 'Basit Faiz = Anapara × Oran × Süre',
        'simple_example_title': 'Örnek:',
        'simple_example': '1.000$ yatırıyorsunuz, 3 yıl boyunca %5 basit faiz:<br>Faiz = 1.000$ × 0,05 × 3 = <strong>150$</strong><br>3 yıl sonra toplam: <strong>1.150$</strong>',
        'what_compound_title': 'Bileşik Faiz Nedir?',
        'what_compound': 'Bileşik faiz, anapara <strong>artı birikmiş faiz</strong> üzerinden hesaplanır. Faiziniz faiz kazanır — onu bu kadar güçlü yapan budur.',
        'compound_formula': 'A = P(1 + r/n)^(nt)',
        'compound_formula_note': 'Burada: A = son tutar, P = anapara, r = oran, n = yıllık bileşik sayısı, t = yıl',
        'compound_example_title': 'Bileşik Faizle Aynı Örnek:',
        'compound_example': '1.000$ yatırıyorsunuz, 3 yıl boyunca yıllık %5 bileşik:<br>Yıl 1: 1.000$ × 1,05 = 1.050$<br>Yıl 2: 1.050$ × 1,05 = 1.102,50$<br>Yıl 3: 1.102,50$ × 1,05 = <strong>1.157,63$</strong>',
        'difference_title': 'Fark: 7,63$ Ekstra',
        'difference': 'Bileşik faizle <strong>157,63$</strong> kazandınız, basit faizle <strong>150$</strong>. Bu %5 daha fazla kazanç! Ve bu fark uzun dönemlerde dramatik şekilde büyür.',
        'table_title': 'Zamana Göre Karşılaştırma (10.000$ %7\'de)',
        'table_years': 'Yıl',
        'table_simple': 'Basit Faiz',
        'table_compound': 'Bileşik Faiz',
        'table_diff': 'Fark',
        'when_title': 'Her Tür Ne Zaman Kullanılır',
        'when_simple_title': 'Basit faiz yaygındır:',
        'when_simple_list': ['Araba kredileri', 'Kısa vadeli bireysel krediler', 'Bazı tahviller', 'Sadece faizli ipotekler'],
        'when_compound_title': 'Bileşik faiz yaygındır:',
        'when_compound_list': ['Tasarruf hesapları', 'Yatırım hesapları', 'Kredi kartları (aleyhinize çalışır!)', 'İpotekler', 'Öğrenci kredileri'],
        'key_title': 'Önemli Noktalar',
        'key_1': '<strong>Tasarruf için:</strong> Bileşik faiz istersiniz — bileşik ne kadar sık olursa o kadar iyi',
        'key_2': '<strong>Krediler için:</strong> Basit faiz zamanla daha az maliyetli',
        'key_3': '<strong>Zaman önemli:</strong> Bileşik faiz avantajları zamanla katlanarak büyür',
        'key_4': '<strong>Erken başlayın:</strong> Bileşik faizle ne kadar erken yatırım yapmaya başlarsanız, sonuçlar o kadar dramatik',
        'cta_title': 'Büyümenizi Hesaplayın',
        'cta_text': 'Paranızın nasıl büyüyebileceğini görmek için ücretsiz bileşik faiz hesaplayıcımızı kullanın.',
        'cta_button': 'Hesaplayıcıyı Aç →',
        'back': '← Hesaplayıcı',
    },
}

# Article 2: Beginner's Guide
BEGINNERS_GUIDE = {
    'en': {
        'title': 'Beginner\'s Guide to Compound Interest | How It Works',
        'meta': 'New to compound interest? Learn how it works, why it\'s called the 8th wonder of the world, and how to use it to build wealth.',
        'h1': 'Beginner\'s Guide to Compound Interest',
        'subtitle': 'The simple concept that can make you wealthy',
        'intro': 'Albert Einstein allegedly called compound interest "the eighth wonder of the world." Whether he said it or not, the power of compounding is <strong>real and remarkable</strong>. Here\'s everything a beginner needs to know.',
        'what_title': 'What is Compound Interest?',
        'what_text': 'Compound interest is when you earn interest on your interest. Instead of just earning returns on your original investment, you earn returns on your returns too.',
        'what_analogy': 'Think of it like a snowball rolling down a hill. It starts small, but as it rolls, it picks up more snow. The bigger it gets, the more snow it picks up with each rotation. Your money works the same way with compound interest.',
        'how_title': 'How Does It Work?',
        'how_step1_title': 'Year 1: You earn interest on your deposit',
        'how_step1': '$1,000 × 10% = $100 interest → Balance: $1,100',
        'how_step2_title': 'Year 2: You earn interest on $1,100 (not just $1,000)',
        'how_step2': '$1,100 × 10% = $110 interest → Balance: $1,210',
        'how_step3_title': 'Year 3: You earn interest on $1,210',
        'how_step3': '$1,210 × 10% = $121 interest → Balance: $1,331',
        'how_note': 'Notice how you earned $100, then $110, then $121? That\'s compounding in action — each year you earn more than the last.',
        'magic_title': 'The Magic of Time',
        'magic_text': 'The real power of compound interest comes from <strong>time</strong>. The longer your money compounds, the more dramatic the results:',
        'magic_table_years': 'Years',
        'magic_table_value': 'Value of $10,000 at 7%',
        'magic_table_earned': 'Interest Earned',
        'rule72_title': 'The Rule of 72',
        'rule72_text': 'A quick way to estimate how long it takes to double your money:',
        'rule72_formula': '72 ÷ Interest Rate = Years to Double',
        'rule72_examples_title': 'Examples:',
        'rule72_examples': ['At 6%: 72 ÷ 6 = 12 years to double', 'At 8%: 72 ÷ 8 = 9 years to double', 'At 10%: 72 ÷ 10 = 7.2 years to double'],
        'frequency_title': 'Compounding Frequency Matters',
        'frequency_text': 'Interest can compound at different intervals:',
        'frequency_list': ['<strong>Annually</strong> — once per year', '<strong>Monthly</strong> — 12 times per year', '<strong>Daily</strong> — 365 times per year', '<strong>Continuously</strong> — constantly'],
        'frequency_note': 'More frequent compounding = slightly higher returns. A savings account compounding daily will earn a bit more than one compounding annually at the same rate.',
        'start_title': 'Why Starting Early Matters',
        'start_text': 'Consider two people:',
        'start_alice': '<strong>Alice</strong> invests $5,000/year from age 25-35 (10 years, $50,000 total), then stops.',
        'start_bob': '<strong>Bob</strong> invests $5,000/year from age 35-65 (30 years, $150,000 total).',
        'start_result': 'At age 65 (assuming 7% returns):<br>Alice has <strong>$602,070</strong><br>Bob has <strong>$540,741</strong>',
        'start_lesson': 'Alice invested less money for fewer years but ended up with more — because she started earlier. Time is your greatest asset.',
        'tips_title': '5 Tips to Maximize Compound Interest',
        'tip1': '<strong>Start now</strong> — The best time to start was yesterday. The second best is today.',
        'tip2': '<strong>Be consistent</strong> — Regular contributions supercharge compounding.',
        'tip3': '<strong>Reinvest dividends</strong> — Don\'t take profits out; let them compound.',
        'tip4': '<strong>Minimize fees</strong> — High fees eat into your returns and compound against you.',
        'tip5': '<strong>Be patient</strong> — Compound interest is a slow burn. The magic happens in the later years.',
        'common_title': 'Where You\'ll Find Compound Interest',
        'common_list': ['Savings accounts', 'Certificates of deposit (CDs)', 'Bonds', 'Stock market investments', 'Retirement accounts (401k, IRA)', 'Real estate appreciation'],
        'warning_title': '⚠️ The Dark Side: Compound Interest on Debt',
        'warning_text': 'Compound interest works against you on debt. Credit card interest compounds, meaning you pay interest on interest. A $5,000 balance at 20% APR, paying only minimums, could take 20+ years to pay off and cost over $8,000 in interest.',
        'cta_title': 'See It In Action',
        'cta_text': 'Play with our compound interest calculator to see how your money could grow.',
        'cta_button': 'Open Calculator →',
        'back': '← Calculator',
    },
    'de': {
        'title': 'Anfängerleitfaden zum Zinseszins | Wie er funktioniert',
        'meta': 'Neu beim Zinseszins? Erfahren Sie, wie er funktioniert, warum er das 8. Weltwunder genannt wird und wie Sie damit Vermögen aufbauen.',
        'h1': 'Anfängerleitfaden zum Zinseszins',
        'subtitle': 'Das einfache Konzept, das Sie wohlhabend machen kann',
        'intro': 'Albert Einstein soll den Zinseszins "das achte Weltwunder" genannt haben. Ob er es gesagt hat oder nicht, die Kraft des Zinseszinses ist <strong>real und bemerkenswert</strong>. Hier ist alles, was ein Anfänger wissen muss.',
        'what_title': 'Was ist Zinseszins?',
        'what_text': 'Zinseszins bedeutet, dass Sie Zinsen auf Ihre Zinsen verdienen. Anstatt nur Rendite auf Ihre ursprüngliche Anlage zu erzielen, verdienen Sie auch Rendite auf Ihre Renditen.',
        'what_analogy': 'Stellen Sie sich einen Schneeball vor, der einen Hügel hinunterrollt. Er beginnt klein, aber beim Rollen nimmt er mehr Schnee auf. Je größer er wird, desto mehr Schnee nimmt er bei jeder Umdrehung auf. Ihr Geld funktioniert mit Zinseszins genauso.',
        'how_title': 'Wie funktioniert es?',
        'how_step1_title': 'Jahr 1: Sie verdienen Zinsen auf Ihre Einlage',
        'how_step1': '1.000 € × 10% = 100 € Zinsen → Guthaben: 1.100 €',
        'how_step2_title': 'Jahr 2: Sie verdienen Zinsen auf 1.100 € (nicht nur 1.000 €)',
        'how_step2': '1.100 € × 10% = 110 € Zinsen → Guthaben: 1.210 €',
        'how_step3_title': 'Jahr 3: Sie verdienen Zinsen auf 1.210 €',
        'how_step3': '1.210 € × 10% = 121 € Zinsen → Guthaben: 1.331 €',
        'how_note': 'Beachten Sie, wie Sie 100 €, dann 110 €, dann 121 € verdient haben? Das ist Zinseszins in Aktion — jedes Jahr verdienen Sie mehr als im Vorjahr.',
        'magic_title': 'Die Magie der Zeit',
        'magic_text': 'Die wahre Kraft des Zinseszinses kommt von der <strong>Zeit</strong>. Je länger Ihr Geld verzinst wird, desto dramatischer die Ergebnisse:',
        'magic_table_years': 'Jahre',
        'magic_table_value': 'Wert von 10.000 € bei 7%',
        'magic_table_earned': 'Verdiente Zinsen',
        'rule72_title': 'Die 72er-Regel',
        'rule72_text': 'Eine schnelle Methode um abzuschätzen, wie lange es dauert, Ihr Geld zu verdoppeln:',
        'rule72_formula': '72 ÷ Zinssatz = Jahre bis zur Verdopplung',
        'rule72_examples_title': 'Beispiele:',
        'rule72_examples': ['Bei 6%: 72 ÷ 6 = 12 Jahre bis zur Verdopplung', 'Bei 8%: 72 ÷ 8 = 9 Jahre bis zur Verdopplung', 'Bei 10%: 72 ÷ 10 = 7,2 Jahre bis zur Verdopplung'],
        'frequency_title': 'Die Häufigkeit der Verzinsung ist wichtig',
        'frequency_text': 'Zinsen können in verschiedenen Intervallen verzinst werden:',
        'frequency_list': ['<strong>Jährlich</strong> — einmal pro Jahr', '<strong>Monatlich</strong> — 12 mal pro Jahr', '<strong>Täglich</strong> — 365 mal pro Jahr', '<strong>Kontinuierlich</strong> — ständig'],
        'frequency_note': 'Häufigere Verzinsung = etwas höhere Rendite. Ein Sparkonto mit täglicher Verzinsung wird etwas mehr einbringen als eines mit jährlicher Verzinsung zum gleichen Zinssatz.',
        'start_title': 'Warum früh anfangen wichtig ist',
        'start_text': 'Betrachten Sie zwei Personen:',
        'start_alice': '<strong>Alice</strong> investiert 5.000 €/Jahr von 25-35 Jahren (10 Jahre, 50.000 € insgesamt), dann hört sie auf.',
        'start_bob': '<strong>Bob</strong> investiert 5.000 €/Jahr von 35-65 Jahren (30 Jahre, 150.000 € insgesamt).',
        'start_result': 'Mit 65 Jahren (bei 7% Rendite):<br>Alice hat <strong>602.070 €</strong><br>Bob hat <strong>540.741 €</strong>',
        'start_lesson': 'Alice investierte weniger Geld über weniger Jahre, hatte aber am Ende mehr — weil sie früher angefangen hat. Zeit ist Ihr größtes Kapital.',
        'tips_title': '5 Tipps zur Maximierung des Zinseszinses',
        'tip1': '<strong>Fangen Sie jetzt an</strong> — Der beste Zeitpunkt zu starten war gestern. Der zweitbeste ist heute.',
        'tip2': '<strong>Seien Sie konsequent</strong> — Regelmäßige Beiträge beschleunigen den Zinseszins.',
        'tip3': '<strong>Reinvestieren Sie Dividenden</strong> — Nehmen Sie keine Gewinne heraus; lassen Sie sie verzinsen.',
        'tip4': '<strong>Minimieren Sie Gebühren</strong> — Hohe Gebühren schmälern Ihre Rendite und wirken gegen Sie.',
        'tip5': '<strong>Seien Sie geduldig</strong> — Zinseszins ist ein langsamer Prozess. Die Magie passiert in den späteren Jahren.',
        'common_title': 'Wo Sie Zinseszins finden',
        'common_list': ['Sparkonten', 'Festgeld', 'Anleihen', 'Aktienmarkt-Investments', 'Rentenkonten', 'Immobilienwertsteigerung'],
        'warning_title': '⚠️ Die Schattenseite: Zinseszins auf Schulden',
        'warning_text': 'Zinseszins wirkt bei Schulden gegen Sie. Kreditkartenzinsen werden verzinst, was bedeutet, dass Sie Zinsen auf Zinsen zahlen. Ein Saldo von 5.000 € bei 20% Zinsen, bei dem nur das Minimum gezahlt wird, könnte über 20 Jahre zur Tilgung benötigen und über 8.000 € an Zinsen kosten.',
        'cta_title': 'Sehen Sie es in Aktion',
        'cta_text': 'Spielen Sie mit unserem Zinseszinsrechner, um zu sehen, wie Ihr Geld wachsen könnte.',
        'cta_button': 'Rechner öffnen →',
        'back': '← Rechner',
    },
    'es': {
        'title': 'Guía para Principiantes sobre el Interés Compuesto | Cómo Funciona',
        'meta': '¿Nuevo en el interés compuesto? Aprende cómo funciona, por qué se llama la 8ª maravilla del mundo y cómo usarlo para crear riqueza.',
        'h1': 'Guía para Principiantes sobre el Interés Compuesto',
        'subtitle': 'El concepto simple que puede hacerte rico',
        'intro': 'Albert Einstein supuestamente llamó al interés compuesto "la octava maravilla del mundo". Lo haya dicho o no, el poder del interés compuesto es <strong>real y notable</strong>. Aquí está todo lo que un principiante necesita saber.',
        'what_title': '¿Qué es el Interés Compuesto?',
        'what_text': 'El interés compuesto es cuando ganas interés sobre tu interés. En lugar de solo ganar rendimientos sobre tu inversión original, también ganas rendimientos sobre tus rendimientos.',
        'what_analogy': 'Piensa en una bola de nieve rodando colina abajo. Empieza pequeña, pero mientras rueda, recoge más nieve. Cuanto más grande se hace, más nieve recoge con cada vuelta. Tu dinero funciona igual con el interés compuesto.',
        'how_title': '¿Cómo Funciona?',
        'how_step1_title': 'Año 1: Ganas interés sobre tu depósito',
        'how_step1': '$1,000 × 10% = $100 de interés → Saldo: $1,100',
        'how_step2_title': 'Año 2: Ganas interés sobre $1,100 (no solo $1,000)',
        'how_step2': '$1,100 × 10% = $110 de interés → Saldo: $1,210',
        'how_step3_title': 'Año 3: Ganas interés sobre $1,210',
        'how_step3': '$1,210 × 10% = $121 de interés → Saldo: $1,331',
        'how_note': '¿Notas cómo ganaste $100, luego $110, luego $121? Eso es la capitalización en acción — cada año ganas más que el anterior.',
        'magic_title': 'La Magia del Tiempo',
        'magic_text': 'El verdadero poder del interés compuesto viene del <strong>tiempo</strong>. Cuanto más tiempo tu dinero se capitaliza, más dramáticos son los resultados:',
        'magic_table_years': 'Años',
        'magic_table_value': 'Valor de $10,000 al 7%',
        'magic_table_earned': 'Interés Ganado',
        'rule72_title': 'La Regla del 72',
        'rule72_text': 'Una forma rápida de estimar cuánto tiempo toma duplicar tu dinero:',
        'rule72_formula': '72 ÷ Tasa de Interés = Años para Duplicar',
        'rule72_examples_title': 'Ejemplos:',
        'rule72_examples': ['Al 6%: 72 ÷ 6 = 12 años para duplicar', 'Al 8%: 72 ÷ 8 = 9 años para duplicar', 'Al 10%: 72 ÷ 10 = 7.2 años para duplicar'],
        'frequency_title': 'La Frecuencia de Capitalización Importa',
        'frequency_text': 'El interés puede capitalizarse en diferentes intervalos:',
        'frequency_list': ['<strong>Anualmente</strong> — una vez al año', '<strong>Mensualmente</strong> — 12 veces al año', '<strong>Diariamente</strong> — 365 veces al año', '<strong>Continuamente</strong> — constantemente'],
        'frequency_note': 'Mayor frecuencia de capitalización = rendimientos ligeramente mayores. Una cuenta de ahorros que capitaliza diariamente ganará un poco más que una que capitaliza anualmente a la misma tasa.',
        'start_title': 'Por Qué Empezar Temprano Importa',
        'start_text': 'Considera dos personas:',
        'start_alice': '<strong>Alice</strong> invierte $5,000/año desde los 25 a 35 años (10 años, $50,000 total), luego se detiene.',
        'start_bob': '<strong>Bob</strong> invierte $5,000/año desde los 35 a 65 años (30 años, $150,000 total).',
        'start_result': 'A los 65 años (asumiendo 7% de rendimiento):<br>Alice tiene <strong>$602,070</strong><br>Bob tiene <strong>$540,741</strong>',
        'start_lesson': 'Alice invirtió menos dinero por menos años pero terminó con más — porque empezó antes. El tiempo es tu mayor activo.',
        'tips_title': '5 Consejos para Maximizar el Interés Compuesto',
        'tip1': '<strong>Empieza ahora</strong> — El mejor momento para empezar fue ayer. El segundo mejor es hoy.',
        'tip2': '<strong>Sé consistente</strong> — Las contribuciones regulares potencian la capitalización.',
        'tip3': '<strong>Reinvierte los dividendos</strong> — No retires las ganancias; déjalas capitalizar.',
        'tip4': '<strong>Minimiza las comisiones</strong> — Las altas comisiones reducen tus rendimientos y se capitalizan en tu contra.',
        'tip5': '<strong>Ten paciencia</strong> — El interés compuesto es un proceso lento. La magia ocurre en los años posteriores.',
        'common_title': 'Dónde Encontrarás Interés Compuesto',
        'common_list': ['Cuentas de ahorro', 'Certificados de depósito', 'Bonos', 'Inversiones en bolsa', 'Cuentas de retiro (401k, IRA)', 'Apreciación inmobiliaria'],
        'warning_title': '⚠️ El Lado Oscuro: Interés Compuesto en Deudas',
        'warning_text': 'El interés compuesto trabaja en tu contra con las deudas. El interés de las tarjetas de crédito se capitaliza, lo que significa que pagas interés sobre el interés. Un saldo de $5,000 al 20% de APR, pagando solo los mínimos, podría tomar más de 20 años para pagar y costar más de $8,000 en intereses.',
        'cta_title': 'Vélo en Acción',
        'cta_text': 'Juega con nuestra calculadora de interés compuesto para ver cómo podría crecer tu dinero.',
        'cta_button': 'Abrir Calculadora →',
        'back': '← Calculadora',
    },
    'fr': {
        'title': 'Guide du Débutant sur les Intérêts Composés | Comment Ça Marche',
        'meta': 'Nouveau aux intérêts composés? Apprenez comment ça fonctionne, pourquoi c\'est appelé la 8e merveille du monde, et comment l\'utiliser pour bâtir votre richesse.',
        'h1': 'Guide du Débutant sur les Intérêts Composés',
        'subtitle': 'Le concept simple qui peut vous rendre riche',
        'intro': 'Albert Einstein aurait appelé les intérêts composés "la huitième merveille du monde". Qu\'il l\'ait dit ou non, le pouvoir de la composition est <strong>réel et remarquable</strong>. Voici tout ce qu\'un débutant doit savoir.',
        'what_title': 'Qu\'est-ce que les Intérêts Composés?',
        'what_text': 'Les intérêts composés, c\'est quand vous gagnez des intérêts sur vos intérêts. Au lieu de gagner des rendements uniquement sur votre investissement initial, vous gagnez aussi des rendements sur vos rendements.',
        'what_analogy': 'Imaginez une boule de neige qui roule sur une colline. Elle commence petite, mais en roulant, elle ramasse plus de neige. Plus elle grossit, plus elle ramasse de neige à chaque rotation. Votre argent fonctionne de la même façon avec les intérêts composés.',
        'how_title': 'Comment Ça Fonctionne?',
        'how_step1_title': 'Année 1: Vous gagnez des intérêts sur votre dépôt',
        'how_step1': '1 000 € × 10% = 100 € d\'intérêts → Solde: 1 100 €',
        'how_step2_title': 'Année 2: Vous gagnez des intérêts sur 1 100 € (pas seulement 1 000 €)',
        'how_step2': '1 100 € × 10% = 110 € d\'intérêts → Solde: 1 210 €',
        'how_step3_title': 'Année 3: Vous gagnez des intérêts sur 1 210 €',
        'how_step3': '1 210 € × 10% = 121 € d\'intérêts → Solde: 1 331 €',
        'how_note': 'Remarquez comment vous avez gagné 100 €, puis 110 €, puis 121 €? C\'est la composition en action — chaque année vous gagnez plus que la précédente.',
        'magic_title': 'La Magie du Temps',
        'magic_text': 'Le vrai pouvoir des intérêts composés vient du <strong>temps</strong>. Plus longtemps votre argent se compose, plus les résultats sont spectaculaires:',
        'magic_table_years': 'Années',
        'magic_table_value': 'Valeur de 10 000 € à 7%',
        'magic_table_earned': 'Intérêts Gagnés',
        'rule72_title': 'La Règle de 72',
        'rule72_text': 'Un moyen rapide d\'estimer combien de temps il faut pour doubler votre argent:',
        'rule72_formula': '72 ÷ Taux d\'Intérêt = Années pour Doubler',
        'rule72_examples_title': 'Exemples:',
        'rule72_examples': ['À 6%: 72 ÷ 6 = 12 ans pour doubler', 'À 8%: 72 ÷ 8 = 9 ans pour doubler', 'À 10%: 72 ÷ 10 = 7,2 ans pour doubler'],
        'frequency_title': 'La Fréquence de Composition Compte',
        'frequency_text': 'Les intérêts peuvent se composer à différents intervalles:',
        'frequency_list': ['<strong>Annuellement</strong> — une fois par an', '<strong>Mensuellement</strong> — 12 fois par an', '<strong>Quotidiennement</strong> — 365 fois par an', '<strong>Continuellement</strong> — constamment'],
        'frequency_note': 'Une composition plus fréquente = des rendements légèrement plus élevés. Un compte d\'épargne composant quotidiennement rapportera un peu plus qu\'un compte composant annuellement au même taux.',
        'start_title': 'Pourquoi Commencer Tôt Est Important',
        'start_text': 'Considérez deux personnes:',
        'start_alice': '<strong>Alice</strong> investit 5 000 €/an de 25 à 35 ans (10 ans, 50 000 € total), puis s\'arrête.',
        'start_bob': '<strong>Bob</strong> investit 5 000 €/an de 35 à 65 ans (30 ans, 150 000 € total).',
        'start_result': 'À 65 ans (avec 7% de rendement):<br>Alice a <strong>602 070 €</strong><br>Bob a <strong>540 741 €</strong>',
        'start_lesson': 'Alice a investi moins d\'argent pendant moins d\'années mais a fini avec plus — parce qu\'elle a commencé plus tôt. Le temps est votre plus grand atout.',
        'tips_title': '5 Conseils pour Maximiser les Intérêts Composés',
        'tip1': '<strong>Commencez maintenant</strong> — Le meilleur moment pour commencer était hier. Le deuxième meilleur est aujourd\'hui.',
        'tip2': '<strong>Soyez constant</strong> — Les contributions régulières boostent la composition.',
        'tip3': '<strong>Réinvestissez les dividendes</strong> — Ne retirez pas les profits; laissez-les se composer.',
        'tip4': '<strong>Minimisez les frais</strong> — Les frais élevés réduisent vos rendements et se composent contre vous.',
        'tip5': '<strong>Soyez patient</strong> — Les intérêts composés sont un processus lent. La magie opère dans les années suivantes.',
        'common_title': 'Où Vous Trouverez des Intérêts Composés',
        'common_list': ['Comptes d\'épargne', 'Certificats de dépôt', 'Obligations', 'Investissements boursiers', 'Comptes retraite', 'Appréciation immobilière'],
        'warning_title': '⚠️ Le Côté Obscur: Intérêts Composés sur les Dettes',
        'warning_text': 'Les intérêts composés jouent contre vous sur les dettes. Les intérêts des cartes de crédit se composent, ce qui signifie que vous payez des intérêts sur les intérêts. Un solde de 5 000 € à 20% de taux, en ne payant que les minimums, pourrait prendre plus de 20 ans à rembourser et coûter plus de 8 000 € d\'intérêts.',
        'cta_title': 'Voyez-le en Action',
        'cta_text': 'Jouez avec notre calculateur d\'intérêts composés pour voir comment votre argent pourrait croître.',
        'cta_button': 'Ouvrir le Calculateur →',
        'back': '← Calculateur',
    },
    'pt': {
        'title': 'Guia do Iniciante sobre Juros Compostos | Como Funciona',
        'meta': 'Novo nos juros compostos? Aprenda como funciona, por que é chamado de 8ª maravilha do mundo e como usá-lo para construir riqueza.',
        'h1': 'Guia do Iniciante sobre Juros Compostos',
        'subtitle': 'O conceito simples que pode te deixar rico',
        'intro': 'Albert Einstein supostamente chamou os juros compostos de "a oitava maravilha do mundo". Tenha ele dito ou não, o poder da composição é <strong>real e notável</strong>. Aqui está tudo que um iniciante precisa saber.',
        'what_title': 'O que são Juros Compostos?',
        'what_text': 'Juros compostos é quando você ganha juros sobre seus juros. Em vez de apenas ganhar retornos sobre seu investimento original, você também ganha retornos sobre seus retornos.',
        'what_analogy': 'Pense em uma bola de neve rolando morro abaixo. Ela começa pequena, mas enquanto rola, pega mais neve. Quanto maior fica, mais neve pega a cada rotação. Seu dinheiro funciona da mesma forma com juros compostos.',
        'how_title': 'Como Funciona?',
        'how_step1_title': 'Ano 1: Você ganha juros sobre seu depósito',
        'how_step1': 'R$1.000 × 10% = R$100 de juros → Saldo: R$1.100',
        'how_step2_title': 'Ano 2: Você ganha juros sobre R$1.100 (não apenas R$1.000)',
        'how_step2': 'R$1.100 × 10% = R$110 de juros → Saldo: R$1.210',
        'how_step3_title': 'Ano 3: Você ganha juros sobre R$1.210',
        'how_step3': 'R$1.210 × 10% = R$121 de juros → Saldo: R$1.331',
        'how_note': 'Percebeu como você ganhou R$100, depois R$110, depois R$121? Isso é a composição em ação — cada ano você ganha mais que o anterior.',
        'magic_title': 'A Mágica do Tempo',
        'magic_text': 'O verdadeiro poder dos juros compostos vem do <strong>tempo</strong>. Quanto mais tempo seu dinheiro compõe, mais dramáticos os resultados:',
        'magic_table_years': 'Anos',
        'magic_table_value': 'Valor de R$10.000 a 7%',
        'magic_table_earned': 'Juros Ganhos',
        'rule72_title': 'A Regra dos 72',
        'rule72_text': 'Uma forma rápida de estimar quanto tempo leva para dobrar seu dinheiro:',
        'rule72_formula': '72 ÷ Taxa de Juros = Anos para Dobrar',
        'rule72_examples_title': 'Exemplos:',
        'rule72_examples': ['A 6%: 72 ÷ 6 = 12 anos para dobrar', 'A 8%: 72 ÷ 8 = 9 anos para dobrar', 'A 10%: 72 ÷ 10 = 7,2 anos para dobrar'],
        'frequency_title': 'A Frequência de Composição Importa',
        'frequency_text': 'Os juros podem compor em diferentes intervalos:',
        'frequency_list': ['<strong>Anualmente</strong> — uma vez por ano', '<strong>Mensalmente</strong> — 12 vezes por ano', '<strong>Diariamente</strong> — 365 vezes por ano', '<strong>Continuamente</strong> — constantemente'],
        'frequency_note': 'Composição mais frequente = retornos ligeiramente maiores. Uma conta poupança que compõe diariamente ganhará um pouco mais que uma que compõe anualmente na mesma taxa.',
        'start_title': 'Por Que Começar Cedo Importa',
        'start_text': 'Considere duas pessoas:',
        'start_alice': '<strong>Alice</strong> investe R$5.000/ano dos 25 aos 35 anos (10 anos, R$50.000 total), depois para.',
        'start_bob': '<strong>Bob</strong> investe R$5.000/ano dos 35 aos 65 anos (30 anos, R$150.000 total).',
        'start_result': 'Aos 65 anos (assumindo 7% de retorno):<br>Alice tem <strong>R$602.070</strong><br>Bob tem <strong>R$540.741</strong>',
        'start_lesson': 'Alice investiu menos dinheiro por menos anos mas terminou com mais — porque começou antes. Tempo é seu maior ativo.',
        'tips_title': '5 Dicas para Maximizar os Juros Compostos',
        'tip1': '<strong>Comece agora</strong> — O melhor momento para começar foi ontem. O segundo melhor é hoje.',
        'tip2': '<strong>Seja consistente</strong> — Contribuições regulares potencializam a composição.',
        'tip3': '<strong>Reinvista os dividendos</strong> — Não retire os lucros; deixe-os compor.',
        'tip4': '<strong>Minimize as taxas</strong> — Taxas altas corroem seus retornos e compõem contra você.',
        'tip5': '<strong>Tenha paciência</strong> — Juros compostos são um processo lento. A mágica acontece nos anos posteriores.',
        'common_title': 'Onde Você Encontrará Juros Compostos',
        'common_list': ['Contas poupança', 'CDBs', 'Títulos', 'Investimentos em ações', 'Contas de aposentadoria', 'Valorização imobiliária'],
        'warning_title': '⚠️ O Lado Sombrio: Juros Compostos em Dívidas',
        'warning_text': 'Juros compostos trabalham contra você em dívidas. Juros de cartão de crédito compõem, significando que você paga juros sobre juros. Um saldo de R$5.000 a 20% ao ano, pagando apenas o mínimo, poderia levar mais de 20 anos para quitar e custar mais de R$8.000 em juros.',
        'cta_title': 'Veja em Ação',
        'cta_text': 'Experimente nossa calculadora de juros compostos para ver como seu dinheiro pode crescer.',
        'cta_button': 'Abrir Calculadora →',
        'back': '← Calculadora',
    },
    'zh': {
        'title': '复利入门指南 | 工作原理',
        'meta': '复利新手？了解它如何运作，为什么被称为世界第八大奇迹，以及如何用它来积累财富。',
        'h1': '复利入门指南',
        'subtitle': '能让你致富的简单概念',
        'intro': '据说阿尔伯特·爱因斯坦称复利为"世界第八大奇迹"。不管他说没说过，复利的力量是<strong>真实而显著的</strong>。这里是初学者需要知道的一切。',
        'what_title': '什么是复利？',
        'what_text': '复利是指你从利息中赚取利息。你不仅从原始投资中获得回报，还从你的回报中获得回报。',
        'what_analogy': '把它想象成一个滚下山的雪球。它开始时很小，但在滚动过程中，它会收集更多的雪。它变得越大，每次旋转收集的雪就越多。你的钱在复利下也是这样工作的。',
        'how_title': '它是如何工作的？',
        'how_step1_title': '第1年：你从存款中赚取利息',
        'how_step1': '1,000美元 × 10% = 100美元利息 → 余额：1,100美元',
        'how_step2_title': '第2年：你从1,100美元（不仅仅是1,000美元）赚取利息',
        'how_step2': '1,100美元 × 10% = 110美元利息 → 余额：1,210美元',
        'how_step3_title': '第3年：你从1,210美元赚取利息',
        'how_step3': '1,210美元 × 10% = 121美元利息 → 余额：1,331美元',
        'how_note': '注意到你赚了100美元，然后110美元，然后121美元吗？这就是复利在起作用——每年你赚的比上一年多。',
        'magic_title': '时间的魔力',
        'magic_text': '复利的真正力量来自于<strong>时间</strong>。你的钱复利的时间越长，结果就越惊人：',
        'magic_table_years': '年数',
        'magic_table_value': '10,000美元在7%下的价值',
        'magic_table_earned': '赚取的利息',
        'rule72_title': '72法则',
        'rule72_text': '快速估算资金翻倍所需时间的方法：',
        'rule72_formula': '72 ÷ 利率 = 翻倍所需年数',
        'rule72_examples_title': '示例：',
        'rule72_examples': ['6%时：72 ÷ 6 = 12年翻倍', '8%时：72 ÷ 8 = 9年翻倍', '10%时：72 ÷ 10 = 7.2年翻倍'],
        'frequency_title': '复利频率很重要',
        'frequency_text': '利息可以按不同间隔复利：',
        'frequency_list': ['<strong>每年</strong> — 每年一次', '<strong>每月</strong> — 每年12次', '<strong>每日</strong> — 每年365次', '<strong>连续</strong> — 持续不断'],
        'frequency_note': '更频繁的复利 = 略高的回报。每日复利的储蓄账户将比同利率下每年复利的账户多赚一点。',
        'start_title': '为什么尽早开始很重要',
        'start_text': '考虑两个人：',
        'start_alice': '<strong>Alice</strong> 从25岁到35岁每年投资5,000美元（10年，共50,000美元），然后停止。',
        'start_bob': '<strong>Bob</strong> 从35岁到65岁每年投资5,000美元（30年，共150,000美元）。',
        'start_result': '在65岁时（假设7%回报）：<br>Alice有<strong>602,070美元</strong><br>Bob有<strong>540,741美元</strong>',
        'start_lesson': 'Alice投资更少的钱，更少的年数，但最终拥有更多——因为她开始得更早。时间是你最大的资产。',
        'tips_title': '最大化复利的5个技巧',
        'tip1': '<strong>现在就开始</strong> — 开始的最佳时间是昨天。第二好的是今天。',
        'tip2': '<strong>保持一致</strong> — 定期投资能增强复利效果。',
        'tip3': '<strong>再投资股息</strong> — 不要取出利润；让它们继续复利。',
        'tip4': '<strong>最小化费用</strong> — 高费用会侵蚀你的回报，并对你产生复利效应。',
        'tip5': '<strong>要有耐心</strong> — 复利是一个缓慢的过程。魔力发生在后来的几年。',
        'common_title': '在哪里可以找到复利',
        'common_list': ['储蓄账户', '定期存款', '债券', '股票市场投资', '退休账户', '房地产增值'],
        'warning_title': '⚠️ 阴暗面：债务上的复利',
        'warning_text': '复利在债务上对你不利。信用卡利息会复利，意味着你在利息上支付利息。5,000美元的余额，年利率20%，只付最低还款额，可能需要20多年才能还清，利息超过8,000美元。',
        'cta_title': '看看实际效果',
        'cta_text': '使用我们的复利计算器，看看你的钱能增长多少。',
        'cta_button': '打开计算器 →',
        'back': '← 计算器',
    },
    'ja': {
        'title': '複利の初心者ガイド | 仕組みを解説',
        'meta': '複利は初めてですか？仕組み、世界第8の不思議と呼ばれる理由、富を築くための活用法を学びましょう。',
        'h1': '複利の初心者ガイド',
        'subtitle': 'あなたを豊かにするシンプルな概念',
        'intro': 'アルバート・アインシュタインは複利を「世界第8の不思議」と呼んだと言われています。彼が言ったかどうかはともかく、複利の力は<strong>本物で驚くべきもの</strong>です。初心者が知っておくべきことをすべてご紹介します。',
        'what_title': '複利とは？',
        'what_text': '複利とは、利息に対して利息が付くことです。元本投資からの利益だけでなく、その利益からも利益を得ることができます。',
        'what_analogy': '丘を転がり落ちる雪玉を想像してください。最初は小さいですが、転がるにつれてより多くの雪を拾います。大きくなればなるほど、一回転ごとにより多くの雪を拾います。複利でのお金も同じように働きます。',
        'how_title': 'どのように機能するの？',
        'how_step1_title': '1年目：預金に対して利息を得る',
        'how_step1': '10万円 × 10% = 1万円の利息 → 残高：11万円',
        'how_step2_title': '2年目：11万円（10万円だけでなく）に対して利息を得る',
        'how_step2': '11万円 × 10% = 1.1万円の利息 → 残高：12.1万円',
        'how_step3_title': '3年目：12.1万円に対して利息を得る',
        'how_step3': '12.1万円 × 10% = 1.21万円の利息 → 残高：13.31万円',
        'how_note': '1万円、1.1万円、1.21万円と稼いだことに気づきましたか？これが複利の実際の働きです — 毎年前年より多く稼ぎます。',
        'magic_title': '時間の魔法',
        'magic_text': '複利の本当の力は<strong>時間</strong>から来ます。お金が複利で運用される期間が長いほど、結果は劇的になります：',
        'magic_table_years': '年数',
        'magic_table_value': '100万円の7%での価値',
        'magic_table_earned': '獲得利息',
        'rule72_title': '72の法則',
        'rule72_text': 'お金が2倍になるまでの時間を素早く見積もる方法：',
        'rule72_formula': '72 ÷ 金利 = 2倍になるまでの年数',
        'rule72_examples_title': '例：',
        'rule72_examples': ['6%の場合：72 ÷ 6 = 12年で2倍', '8%の場合：72 ÷ 8 = 9年で2倍', '10%の場合：72 ÷ 10 = 7.2年で2倍'],
        'frequency_title': '複利の頻度が重要',
        'frequency_text': '利息は異なる間隔で複利計算できます：',
        'frequency_list': ['<strong>年次</strong> — 年1回', '<strong>月次</strong> — 年12回', '<strong>日次</strong> — 年365回', '<strong>連続</strong> — 常時'],
        'frequency_note': 'より頻繁な複利 = わずかに高いリターン。日次複利の普通預金は、同じ金利で年次複利のものより少し多く稼げます。',
        'start_title': 'なぜ早く始めることが重要か',
        'start_text': '2人を考えてみましょう：',
        'start_alice': '<strong>Alice</strong>は25歳から35歳まで年間50万円を投資（10年間、合計500万円）し、その後やめます。',
        'start_bob': '<strong>Bob</strong>は35歳から65歳まで年間50万円を投資（30年間、合計1500万円）します。',
        'start_result': '65歳時点で（7%のリターンを想定）：<br>Aliceは<strong>約6,000万円</strong><br>Bobは<strong>約5,400万円</strong>',
        'start_lesson': 'Aliceはより少ないお金をより短い期間投資しましたが、最終的にはより多くを持っています — 早く始めたからです。時間はあなたの最大の資産です。',
        'tips_title': '複利を最大化する5つのヒント',
        'tip1': '<strong>今すぐ始める</strong> — 始めるのに最適な時期は昨日でした。次に良いのは今日です。',
        'tip2': '<strong>一貫性を保つ</strong> — 定期的な積立が複利効果を加速させます。',
        'tip3': '<strong>配当を再投資する</strong> — 利益を引き出さず、複利で運用しましょう。',
        'tip4': '<strong>手数料を最小限に</strong> — 高い手数料はリターンを蝕み、あなたに不利に複利効果を発揮します。',
        'tip5': '<strong>忍耐強く</strong> — 複利はゆっくりとしたプロセスです。魔法は後年に起こります。',
        'common_title': '複利が見られる場所',
        'common_list': ['普通預金', '定期預金', '債券', '株式市場投資', '退職口座（401k、IRA）', '不動産価値上昇'],
        'warning_title': '⚠️ ダークサイド：借金の複利',
        'warning_text': '複利は借金では不利に働きます。クレジットカードの利息は複利なので、利息に利息を払うことになります。50万円の残高で年利20%、最低支払いだけでは、返済に20年以上かかり、利息だけで80万円以上かかる可能性があります。',
        'cta_title': '実際に見てみよう',
        'cta_text': '複利計算機で、あなたのお金がどれだけ成長できるか確認しましょう。',
        'cta_button': '計算機を開く →',
        'back': '← 計算機',
    },
    'ru': {
        'title': 'Руководство для Начинающих по Сложным Процентам | Как Это Работает',
        'meta': 'Новичок в сложных процентах? Узнайте, как это работает, почему это называют 8-м чудом света, и как использовать их для накопления богатства.',
        'h1': 'Руководство для Начинающих по Сложным Процентам',
        'subtitle': 'Простая концепция, которая может сделать вас богатым',
        'intro': 'Альберт Эйнштейн якобы назвал сложные проценты "восьмым чудом света". Сказал он это или нет, сила сложных процентов <strong>реальна и замечательна</strong>. Вот всё, что нужно знать начинающему.',
        'what_title': 'Что такое Сложные Проценты?',
        'what_text': 'Сложные проценты — это когда вы зарабатываете проценты на своих процентах. Вместо того чтобы получать доход только от первоначальной инвестиции, вы также получаете доход от своих доходов.',
        'what_analogy': 'Представьте снежок, катящийся с горы. Он начинается маленьким, но по мере качения собирает больше снега. Чем больше он становится, тем больше снега собирает с каждым оборотом. Ваши деньги работают так же со сложными процентами.',
        'how_title': 'Как Это Работает?',
        'how_step1_title': 'Год 1: Вы зарабатываете проценты на своём вкладе',
        'how_step1': '$1,000 × 10% = $100 процентов → Баланс: $1,100',
        'how_step2_title': 'Год 2: Вы зарабатываете проценты на $1,100 (не только на $1,000)',
        'how_step2': '$1,100 × 10% = $110 процентов → Баланс: $1,210',
        'how_step3_title': 'Год 3: Вы зарабатываете проценты на $1,210',
        'how_step3': '$1,210 × 10% = $121 процентов → Баланс: $1,331',
        'how_note': 'Заметили, как вы заработали $100, потом $110, потом $121? Это сложные проценты в действии — каждый год вы зарабатываете больше, чем в предыдущий.',
        'magic_title': 'Магия Времени',
        'magic_text': 'Настоящая сила сложных процентов исходит от <strong>времени</strong>. Чем дольше ваши деньги накапливаются, тем более впечатляющие результаты:',
        'magic_table_years': 'Лет',
        'magic_table_value': 'Стоимость $10,000 при 7%',
        'magic_table_earned': 'Заработано Процентов',
        'rule72_title': 'Правило 72',
        'rule72_text': 'Быстрый способ оценить, сколько времени нужно для удвоения денег:',
        'rule72_formula': '72 ÷ Процентная Ставка = Лет до Удвоения',
        'rule72_examples_title': 'Примеры:',
        'rule72_examples': ['При 6%: 72 ÷ 6 = 12 лет до удвоения', 'При 8%: 72 ÷ 8 = 9 лет до удвоения', 'При 10%: 72 ÷ 10 = 7.2 лет до удвоения'],
        'frequency_title': 'Частота Начисления Важна',
        'frequency_text': 'Проценты могут начисляться с разной периодичностью:',
        'frequency_list': ['<strong>Ежегодно</strong> — раз в год', '<strong>Ежемесячно</strong> — 12 раз в год', '<strong>Ежедневно</strong> — 365 раз в год', '<strong>Непрерывно</strong> — постоянно'],
        'frequency_note': 'Более частое начисление = немного более высокая доходность. Сберегательный счёт с ежедневным начислением заработает чуть больше, чем с ежегодным при той же ставке.',
        'start_title': 'Почему Важно Начать Рано',
        'start_text': 'Рассмотрим двух человек:',
        'start_alice': '<strong>Алиса</strong> инвестирует $5,000/год с 25 до 35 лет (10 лет, всего $50,000), затем прекращает.',
        'start_bob': '<strong>Боб</strong> инвестирует $5,000/год с 35 до 65 лет (30 лет, всего $150,000).',
        'start_result': 'В 65 лет (при 7% доходности):<br>Алиса имеет <strong>$602,070</strong><br>Боб имеет <strong>$540,741</strong>',
        'start_lesson': 'Алиса инвестировала меньше денег за меньшее время, но в итоге получила больше — потому что начала раньше. Время — ваш главный актив.',
        'tips_title': '5 Советов для Максимизации Сложных Процентов',
        'tip1': '<strong>Начните сейчас</strong> — Лучшее время начать было вчера. Второе лучшее — сегодня.',
        'tip2': '<strong>Будьте последовательны</strong> — Регулярные взносы усиливают эффект сложных процентов.',
        'tip3': '<strong>Реинвестируйте дивиденды</strong> — Не выводите прибыль; пусть она накапливается.',
        'tip4': '<strong>Минимизируйте комиссии</strong> — Высокие комиссии съедают вашу доходность и работают против вас.',
        'tip5': '<strong>Будьте терпеливы</strong> — Сложные проценты — медленный процесс. Магия происходит в последующие годы.',
        'common_title': 'Где Вы Найдёте Сложные Проценты',
        'common_list': ['Сберегательные счета', 'Депозитные сертификаты', 'Облигации', 'Инвестиции на фондовом рынке', 'Пенсионные счета', 'Рост стоимости недвижимости'],
        'warning_title': '⚠️ Тёмная Сторона: Сложные Проценты на Долги',
        'warning_text': 'Сложные проценты работают против вас при долгах. Проценты по кредитной карте накапливаются, то есть вы платите проценты на проценты. Баланс в $5,000 при 20% годовых, при оплате только минимума, может потребовать более 20 лет для погашения и стоить более $8,000 в процентах.',
        'cta_title': 'Увидьте Это в Действии',
        'cta_text': 'Поиграйте с нашим калькулятором сложных процентов, чтобы увидеть, как могут расти ваши деньги.',
        'cta_button': 'Открыть Калькулятор →',
        'back': '← Калькулятор',
    },
    'hi': {
        'title': 'चक्रवृद्धि ब्याज की शुरुआती गाइड | यह कैसे काम करता है',
        'meta': 'चक्रवृद्धि ब्याज में नए हैं? जानें कि यह कैसे काम करता है, इसे दुनिया का 8वां अजूबा क्यों कहा जाता है, और धन बनाने के लिए इसका उपयोग कैसे करें।',
        'h1': 'चक्रवृद्धि ब्याज की शुरुआती गाइड',
        'subtitle': 'वह सरल अवधारणा जो आपको अमीर बना सकती है',
        'intro': 'कहा जाता है कि अल्बर्ट आइंस्टीन ने चक्रवृद्धि ब्याज को "दुनिया का आठवां अजूबा" कहा था। उन्होंने कहा हो या नहीं, चक्रवृद्धि की शक्ति <strong>वास्तविक और उल्लेखनीय</strong> है। यहां वह सब कुछ है जो एक शुरुआती को जानना चाहिए।',
        'what_title': 'चक्रवृद्धि ब्याज क्या है?',
        'what_text': 'चक्रवृद्धि ब्याज तब होता है जब आप अपने ब्याज पर ब्याज कमाते हैं। केवल अपने मूल निवेश पर रिटर्न कमाने के बजाय, आप अपने रिटर्न पर भी रिटर्न कमाते हैं।',
        'what_analogy': 'इसे एक पहाड़ी से लुढ़कती स्नोबॉल की तरह सोचें। यह छोटी शुरू होती है, लेकिन जैसे-जैसे लुढ़कती है, अधिक बर्फ उठाती है। यह जितनी बड़ी होती है, हर घुमाव के साथ उतनी ही अधिक बर्फ उठाती है। चक्रवृद्धि ब्याज के साथ आपका पैसा भी इसी तरह काम करता है।',
        'how_title': 'यह कैसे काम करता है?',
        'how_step1_title': 'वर्ष 1: आप अपनी जमा पर ब्याज कमाते हैं',
        'how_step1': '₹1,000 × 10% = ₹100 ब्याज → शेष: ₹1,100',
        'how_step2_title': 'वर्ष 2: आप ₹1,100 पर ब्याज कमाते हैं (केवल ₹1,000 पर नहीं)',
        'how_step2': '₹1,100 × 10% = ₹110 ब्याज → शेष: ₹1,210',
        'how_step3_title': 'वर्ष 3: आप ₹1,210 पर ब्याज कमाते हैं',
        'how_step3': '₹1,210 × 10% = ₹121 ब्याज → शेष: ₹1,331',
        'how_note': 'देखा कैसे आपने ₹100, फिर ₹110, फिर ₹121 कमाए? यह चक्रवृद्धि क्रिया में है — हर साल आप पिछले साल से अधिक कमाते हैं।',
        'magic_title': 'समय का जादू',
        'magic_text': 'चक्रवृद्धि ब्याज की असली शक्ति <strong>समय</strong> से आती है। आपका पैसा जितना लंबा चक्रवृद्धि होता है, परिणाम उतने ही नाटकीय होते हैं:',
        'magic_table_years': 'वर्ष',
        'magic_table_value': '7% पर ₹10,000 का मूल्य',
        'magic_table_earned': 'अर्जित ब्याज',
        'rule72_title': '72 का नियम',
        'rule72_text': 'यह अनुमान लगाने का एक त्वरित तरीका है कि आपका पैसा दोगुना होने में कितना समय लगता है:',
        'rule72_formula': '72 ÷ ब्याज दर = दोगुना होने के लिए वर्ष',
        'rule72_examples_title': 'उदाहरण:',
        'rule72_examples': ['6% पर: 72 ÷ 6 = 12 वर्ष में दोगुना', '8% पर: 72 ÷ 8 = 9 वर्ष में दोगुना', '10% पर: 72 ÷ 10 = 7.2 वर्ष में दोगुना'],
        'frequency_title': 'चक्रवृद्धि आवृत्ति मायने रखती है',
        'frequency_text': 'ब्याज विभिन्न अंतरालों पर चक्रवृद्धि हो सकता है:',
        'frequency_list': ['<strong>वार्षिक</strong> — प्रति वर्ष एक बार', '<strong>मासिक</strong> — प्रति वर्ष 12 बार', '<strong>दैनिक</strong> — प्रति वर्ष 365 बार', '<strong>निरंतर</strong> — लगातार'],
        'frequency_note': 'अधिक बार चक्रवृद्धि = थोड़ा अधिक रिटर्न। दैनिक चक्रवृद्धि वाला बचत खाता समान दर पर वार्षिक चक्रवृद्धि वाले से थोड़ा अधिक कमाएगा।',
        'start_title': 'जल्दी शुरू करना क्यों मायने रखता है',
        'start_text': 'दो लोगों पर विचार करें:',
        'start_alice': '<strong>Alice</strong> 25 से 35 वर्ष की आयु तक ₹5,000/वर्ष निवेश करती है (10 वर्ष, कुल ₹50,000), फिर रुक जाती है।',
        'start_bob': '<strong>Bob</strong> 35 से 65 वर्ष की आयु तक ₹5,000/वर्ष निवेश करता है (30 वर्ष, कुल ₹1,50,000)।',
        'start_result': '65 वर्ष की आयु में (7% रिटर्न मानते हुए):<br>Alice के पास <strong>₹6,02,070</strong> हैं<br>Bob के पास <strong>₹5,40,741</strong> हैं',
        'start_lesson': 'Alice ने कम पैसे कम वर्षों के लिए निवेश किए लेकिन अधिक के साथ समाप्त हुई — क्योंकि उसने जल्दी शुरू किया। समय आपकी सबसे बड़ी संपत्ति है।',
        'tips_title': 'चक्रवृद्धि ब्याज को अधिकतम करने के लिए 5 टिप्स',
        'tip1': '<strong>अभी शुरू करें</strong> — शुरू करने का सबसे अच्छा समय कल था। दूसरा सबसे अच्छा आज है।',
        'tip2': '<strong>सुसंगत रहें</strong> — नियमित योगदान चक्रवृद्धि को तेज करता है।',
        'tip3': '<strong>लाभांश पुनर्निवेश करें</strong> — मुनाफा न निकालें; उन्हें चक्रवृद्धि होने दें।',
        'tip4': '<strong>शुल्क कम करें</strong> — उच्च शुल्क आपके रिटर्न को खा जाते हैं और आपके खिलाफ चक्रवृद्धि होते हैं।',
        'tip5': '<strong>धैर्य रखें</strong> — चक्रवृद्धि ब्याज एक धीमी प्रक्रिया है। जादू बाद के वर्षों में होता है।',
        'common_title': 'आप चक्रवृद्धि ब्याज कहां पाएंगे',
        'common_list': ['बचत खाते', 'सावधि जमा (FD)', 'बॉन्ड', 'शेयर बाजार निवेश', 'सेवानिवृत्ति खाते', 'रियल एस्टेट मूल्यवृद्धि'],
        'warning_title': '⚠️ अंधेरा पक्ष: कर्ज पर चक्रवृद्धि ब्याज',
        'warning_text': 'चक्रवृद्धि ब्याज कर्ज पर आपके खिलाफ काम करता है। क्रेडिट कार्ड ब्याज चक्रवृद्धि होता है, यानी आप ब्याज पर ब्याज देते हैं। ₹5,000 का बैलेंस 20% APR पर, केवल न्यूनतम भुगतान करने पर, चुकाने में 20+ साल लग सकते हैं और ब्याज में ₹8,000 से अधिक खर्च हो सकता है।',
        'cta_title': 'इसे क्रिया में देखें',
        'cta_text': 'हमारे चक्रवृद्धि ब्याज कैलकुलेटर के साथ खेलें और देखें कि आपका पैसा कैसे बढ़ सकता है।',
        'cta_button': 'कैलकुलेटर खोलें →',
        'back': '← कैलकुलेटर',
    },
    'ar': {
        'title': 'دليل المبتدئين للفائدة المركبة | كيف تعمل',
        'meta': 'جديد على الفائدة المركبة؟ تعلم كيف تعمل، ولماذا تسمى الأعجوبة الثامنة في العالم، وكيف تستخدمها لبناء الثروة.',
        'h1': 'دليل المبتدئين للفائدة المركبة',
        'subtitle': 'المفهوم البسيط الذي يمكن أن يجعلك غنياً',
        'intro': 'يُقال إن ألبرت أينشتاين وصف الفائدة المركبة بـ"الأعجوبة الثامنة في العالم". سواء قالها أم لا، فإن قوة التركيب <strong>حقيقية ومذهلة</strong>. إليك كل ما يحتاج المبتدئ معرفته.',
        'what_title': 'ما هي الفائدة المركبة؟',
        'what_text': 'الفائدة المركبة هي عندما تكسب فائدة على فائدتك. بدلاً من كسب عوائد فقط على استثمارك الأصلي، تكسب عوائد على عوائدك أيضاً.',
        'what_analogy': 'فكر بها ككرة ثلج تتدحرج على تل. تبدأ صغيرة، لكن أثناء التدحرج تلتقط المزيد من الثلج. كلما كبرت، التقطت المزيد مع كل دورة. أموالك تعمل بنفس الطريقة مع الفائدة المركبة.',
        'how_title': 'كيف تعمل؟',
        'how_step1_title': 'السنة 1: تكسب فائدة على إيداعك',
        'how_step1': '1,000$ × 10% = 100$ فائدة → الرصيد: 1,100$',
        'how_step2_title': 'السنة 2: تكسب فائدة على 1,100$ (ليس فقط 1,000$)',
        'how_step2': '1,100$ × 10% = 110$ فائدة → الرصيد: 1,210$',
        'how_step3_title': 'السنة 3: تكسب فائدة على 1,210$',
        'how_step3': '1,210$ × 10% = 121$ فائدة → الرصيد: 1,331$',
        'how_note': 'لاحظ كيف كسبت 100$، ثم 110$، ثم 121$؟ هذا هو التركيب في العمل — كل سنة تكسب أكثر من السابقة.',
        'magic_title': 'سحر الوقت',
        'magic_text': 'القوة الحقيقية للفائدة المركبة تأتي من <strong>الوقت</strong>. كلما طالت فترة تركيب أموالك، كانت النتائج أكثر دراماتيكية:',
        'magic_table_years': 'السنوات',
        'magic_table_value': 'قيمة 10,000$ بنسبة 7%',
        'magic_table_earned': 'الفائدة المكتسبة',
        'rule72_title': 'قاعدة 72',
        'rule72_text': 'طريقة سريعة لتقدير المدة اللازمة لمضاعفة أموالك:',
        'rule72_formula': '72 ÷ معدل الفائدة = سنوات للمضاعفة',
        'rule72_examples_title': 'أمثلة:',
        'rule72_examples': ['عند 6%: 72 ÷ 6 = 12 سنة للمضاعفة', 'عند 8%: 72 ÷ 8 = 9 سنوات للمضاعفة', 'عند 10%: 72 ÷ 10 = 7.2 سنة للمضاعفة'],
        'frequency_title': 'تكرار التركيب مهم',
        'frequency_text': 'يمكن أن تتركب الفائدة على فترات مختلفة:',
        'frequency_list': ['<strong>سنوياً</strong> — مرة في السنة', '<strong>شهرياً</strong> — 12 مرة في السنة', '<strong>يومياً</strong> — 365 مرة في السنة', '<strong>باستمرار</strong> — دائماً'],
        'frequency_note': 'تركيب أكثر تكراراً = عوائد أعلى قليلاً. حساب توفير يتركب يومياً سيكسب أكثر قليلاً من حساب يتركب سنوياً بنفس المعدل.',
        'start_title': 'لماذا البدء مبكراً مهم',
        'start_text': 'فكر في شخصين:',
        'start_alice': '<strong>أليس</strong> تستثمر 5,000$/سنة من عمر 25-35 (10 سنوات، 50,000$ إجمالي)، ثم تتوقف.',
        'start_bob': '<strong>بوب</strong> يستثمر 5,000$/سنة من عمر 35-65 (30 سنة، 150,000$ إجمالي).',
        'start_result': 'عند عمر 65 (بافتراض 7% عوائد):<br>أليس لديها <strong>602,070$</strong><br>بوب لديه <strong>540,741$</strong>',
        'start_lesson': 'أليس استثمرت أموالاً أقل لسنوات أقل لكنها انتهت بأكثر — لأنها بدأت مبكراً. الوقت هو أعظم أصولك.',
        'tips_title': '5 نصائح لتعظيم الفائدة المركبة',
        'tip1': '<strong>ابدأ الآن</strong> — أفضل وقت للبدء كان أمس. ثاني أفضل وقت هو اليوم.',
        'tip2': '<strong>كن منتظماً</strong> — المساهمات المنتظمة تعزز التركيب.',
        'tip3': '<strong>أعد استثمار الأرباح</strong> — لا تسحب الأرباح؛ دعها تتركب.',
        'tip4': '<strong>قلل الرسوم</strong> — الرسوم العالية تأكل عوائدك وتتركب ضدك.',
        'tip5': '<strong>كن صبوراً</strong> — الفائدة المركبة عملية بطيئة. السحر يحدث في السنوات اللاحقة.',
        'common_title': 'أين ستجد الفائدة المركبة',
        'common_list': ['حسابات التوفير', 'شهادات الإيداع', 'السندات', 'استثمارات سوق الأسهم', 'حسابات التقاعد', 'ارتفاع قيمة العقارات'],
        'warning_title': '⚠️ الجانب المظلم: الفائدة المركبة على الديون',
        'warning_text': 'الفائدة المركبة تعمل ضدك على الديون. فائدة بطاقات الائتمان تتركب، مما يعني أنك تدفع فائدة على الفائدة. رصيد 5,000$ بنسبة 20% سنوياً، مع دفع الحد الأدنى فقط، قد يستغرق أكثر من 20 سنة للسداد ويكلف أكثر من 8,000$ كفوائد.',
        'cta_title': 'شاهدها في العمل',
        'cta_text': 'العب مع حاسبة الفائدة المركبة لترى كيف يمكن أن تنمو أموالك.',
        'cta_button': 'افتح الحاسبة →',
        'back': '← الحاسبة',
    },
    'tr': {
        'title': 'Bileşik Faiz Başlangıç Rehberi | Nasıl Çalışır',
        'meta': 'Bileşik faizde yeni misiniz? Nasıl çalıştığını, neden dünyanın 8. harikası dendiğini ve servet oluşturmak için nasıl kullanılacağını öğrenin.',
        'h1': 'Bileşik Faiz Başlangıç Rehberi',
        'subtitle': 'Sizi zengin yapabilecek basit kavram',
        'intro': 'Albert Einstein\'ın bileşik faizi "dünyanın sekizinci harikası" dediği söylenir. Söylemiş olsun ya da olmasın, bileşik faizin gücü <strong>gerçek ve dikkat çekici</strong>. İşte bir başlangıcın bilmesi gereken her şey.',
        'what_title': 'Bileşik Faiz Nedir?',
        'what_text': 'Bileşik faiz, faiziniz üzerinden faiz kazandığınız zamandır. Sadece orijinal yatırımınızdan getiri elde etmek yerine, getirilerinizden de getiri elde edersiniz.',
        'what_analogy': 'Tepeden aşağı yuvarlanan bir kar topu gibi düşünün. Küçük başlar, ama yuvarlandıkça daha fazla kar toplar. Büyüdükçe, her dönüşte daha fazla kar toplar. Bileşik faizle paranız da aynı şekilde çalışır.',
        'how_title': 'Nasıl Çalışır?',
        'how_step1_title': 'Yıl 1: Yatırımınız üzerinden faiz kazanırsınız',
        'how_step1': '1.000$ × %10 = 100$ faiz → Bakiye: 1.100$',
        'how_step2_title': 'Yıl 2: 1.100$ üzerinden faiz kazanırsınız (sadece 1.000$ değil)',
        'how_step2': '1.100$ × %10 = 110$ faiz → Bakiye: 1.210$',
        'how_step3_title': 'Yıl 3: 1.210$ üzerinden faiz kazanırsınız',
        'how_step3': '1.210$ × %10 = 121$ faiz → Bakiye: 1.331$',
        'how_note': '100$, sonra 110$, sonra 121$ kazandığınızı fark ettiniz mi? İşte bileşik faiz iş başında — her yıl öncekinden daha fazla kazanırsınız.',
        'magic_title': 'Zamanın Büyüsü',
        'magic_text': 'Bileşik faizin gerçek gücü <strong>zaman</strong>dan gelir. Paranız ne kadar uzun süre bileşik faizle çalışırsa, sonuçlar o kadar dramatik olur:',
        'magic_table_years': 'Yıl',
        'magic_table_value': '%7\'de 10.000$\'ın Değeri',
        'magic_table_earned': 'Kazanılan Faiz',
        'rule72_title': '72 Kuralı',
        'rule72_text': 'Paranızı ikiye katlamanın ne kadar süreceğini tahmin etmenin hızlı bir yolu:',
        'rule72_formula': '72 ÷ Faiz Oranı = İkiye Katlanma Yılı',
        'rule72_examples_title': 'Örnekler:',
        'rule72_examples': ['%6\'da: 72 ÷ 6 = 12 yılda ikiye katlanır', '%8\'de: 72 ÷ 8 = 9 yılda ikiye katlanır', '%10\'da: 72 ÷ 10 = 7,2 yılda ikiye katlanır'],
        'frequency_title': 'Bileşik Sıklığı Önemli',
        'frequency_text': 'Faiz farklı aralıklarla bileşik olabilir:',
        'frequency_list': ['<strong>Yıllık</strong> — yılda bir', '<strong>Aylık</strong> — yılda 12 kez', '<strong>Günlük</strong> — yılda 365 kez', '<strong>Sürekli</strong> — devamlı'],
        'frequency_note': 'Daha sık bileşik = biraz daha yüksek getiri. Günlük bileşik tasarruf hesabı, aynı oranda yıllık bileşikten biraz daha fazla kazanır.',
        'start_title': 'Neden Erken Başlamak Önemli',
        'start_text': 'İki kişiyi düşünün:',
        'start_alice': '<strong>Alice</strong> 25-35 yaş arası yılda 5.000$ yatırım yapar (10 yıl, toplam 50.000$), sonra durur.',
        'start_bob': '<strong>Bob</strong> 35-65 yaş arası yılda 5.000$ yatırım yapar (30 yıl, toplam 150.000$).',
        'start_result': '65 yaşında (%7 getiri varsayılarak):<br>Alice\'in <strong>602.070$</strong>\'ı var<br>Bob\'un <strong>540.741$</strong>\'ı var',
        'start_lesson': 'Alice daha az parayı daha az yıl yatırdı ama daha fazlasıyla bitirdi — çünkü daha erken başladı. Zaman en büyük varlığınızdır.',
        'tips_title': 'Bileşik Faizi Maksimize Etmek İçin 5 İpucu',
        'tip1': '<strong>Şimdi başlayın</strong> — Başlamanın en iyi zamanı dündü. İkinci en iyisi bugün.',
        'tip2': '<strong>Tutarlı olun</strong> — Düzenli katkılar bileşik faizi hızlandırır.',
        'tip3': '<strong>Temettüleri yeniden yatırın</strong> — Kârları çıkarmayın; bileşik olsunlar.',
        'tip4': '<strong>Ücretleri minimize edin</strong> — Yüksek ücretler getirilerinizi yer ve aleyhinize bileşik olur.',
        'tip5': '<strong>Sabırlı olun</strong> — Bileşik faiz yavaş bir süreçtir. Sihir sonraki yıllarda gerçekleşir.',
        'common_title': 'Bileşik Faizi Nerede Bulursunuz',
        'common_list': ['Tasarruf hesapları', 'Mevduat sertifikaları', 'Tahviller', 'Borsa yatırımları', 'Emeklilik hesapları', 'Gayrimenkul değer artışı'],
        'warning_title': '⚠️ Karanlık Taraf: Borçta Bileşik Faiz',
        'warning_text': 'Bileşik faiz borçta aleyhinize çalışır. Kredi kartı faizi bileşik olur, yani faiz üzerine faiz ödersiniz. %20 APR\'de 5.000$ bakiye, sadece minimumları ödeyerek, ödemesi 20+ yıl sürebilir ve 8.000$\'dan fazla faiz maliyeti olabilir.',
        'cta_title': 'Eylemde Görün',
        'cta_text': 'Paranızın nasıl büyüyebileceğini görmek için bileşik faiz hesaplayıcımızla oynayın.',
        'cta_button': 'Hesaplayıcıyı Aç →',
        'back': '← Hesaplayıcı',
    },
}


def generate_article_html(t, article_slug, lang, calc_url):
    """Generate HTML for an article."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    <link rel="canonical" href="https://compoundcalc.ai/articles/{article_slug}/{lang if lang != 'en' else ''}">
    
    <meta property="og:title" content="{t['h1']}">
    <meta property="og:description" content="{t['meta']}">
    <meta property="og:type" content="article">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{t['h1']}","description":"{t['meta']}","author":{{"@type":"Organization","name":"CompoundCalc.ai"}},"publisher":{{"@type":"Organization","name":"CompoundCalc.ai"}},"datePublished":"2026-02-20","dateModified":"2026-02-20"}}
    </script>
    
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%236366f1'/%3E%3Ctext x='50' y='68' font-size='50' text-anchor='middle' fill='white'%3E📈%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
        .prose {{ line-height: 1.8; }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #818cf8; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #c4b5fd; }}
        .prose p {{ margin-bottom: 1rem; color: #cbd5e1; }}
        .prose ul, .prose ol {{ margin-left: 1.5rem; margin-bottom: 1rem; color: #cbd5e1; }}
        .prose ul {{ list-style: disc; }}
        .prose ol {{ list-style: decimal; }}
        .prose li {{ margin-bottom: 0.5rem; }}
        .prose strong {{ color: #f1f5f9; }}
        .formula {{ background: rgba(99,102,241,0.2); border: 1px solid rgba(99,102,241,0.4); padding: 1rem; border-radius: 0.75rem; font-family: monospace; text-align: center; margin: 1rem 0; }}
    </style>
    
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-540W3EEBWX"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-540W3EEBWX');</script>
</head>
<body class="text-white">
    <header class="py-6 px-4">
        <div class="max-w-3xl mx-auto flex items-center justify-between">
            <a href="{calc_url}" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-600 flex items-center justify-center text-xl">📈</div>
                <span class="text-xl font-bold">CompoundCalc</span>
            </a>
            <a href="{calc_url}" class="text-indigo-400 hover:text-indigo-300 text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-16">
        <article class="max-w-3xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl md:text-4xl font-bold mb-4">{t['h1']}</h1>
                <p class="text-slate-400">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-10 prose">
                <p class="text-lg">{t['intro']}</p>
                
                <!-- Content will be article-specific -->
            </div>
        </article>
    </main>

    <footer class="py-8 px-4 border-t border-white/10">
        <div class="max-w-3xl mx-auto text-center text-slate-500 text-sm">
            <p>© 2026 CompoundCalc.ai</p>
        </div>
    </footer>
</body>
</html>'''


def generate_compound_vs_simple(t, lang, calc_url):
    """Generate compound vs simple article."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    
    # Build when lists
    when_simple_items = ''.join([f'<li>{item}</li>' for item in t['when_simple_list']])
    when_compound_items = ''.join([f'<li>{item}</li>' for item in t['when_compound_list']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    <link rel="canonical" href="https://compoundcalc.ai/articles/compound-vs-simple/{'' if lang == 'en' else lang + '/'}">
    
    <meta property="og:title" content="{t['h1']}">
    <meta property="og:description" content="{t['meta']}">
    <meta property="og:type" content="article">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{t['h1']}","description":"{t['meta']}","author":{{"@type":"Organization","name":"CompoundCalc.ai"}},"publisher":{{"@type":"Organization","name":"CompoundCalc.ai"}},"datePublished":"2026-02-20","dateModified":"2026-02-20"}}
    </script>
    
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%236366f1'/%3E%3Ctext x='50' y='68' font-size='50' text-anchor='middle' fill='white'%3E📈%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
        .prose {{ line-height: 1.8; }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #818cf8; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #c4b5fd; }}
        .prose p {{ margin-bottom: 1rem; color: #cbd5e1; }}
        .prose ul {{ list-style: disc; margin-left: 1.5rem; margin-bottom: 1rem; color: #cbd5e1; }}
        .prose li {{ margin-bottom: 0.5rem; }}
        .prose strong {{ color: #f1f5f9; }}
        .formula {{ background: rgba(99,102,241,0.2); border: 1px solid rgba(99,102,241,0.4); padding: 1rem; border-radius: 0.75rem; font-family: monospace; text-align: center; margin: 1rem 0; color: #c4b5fd; }}
    </style>
    
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-540W3EEBWX"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-540W3EEBWX');</script>
</head>
<body class="text-white">
    <header class="py-6 px-4">
        <div class="max-w-3xl mx-auto flex items-center justify-between">
            <a href="{calc_url}" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-600 flex items-center justify-center text-xl">📈</div>
                <span class="text-xl font-bold">CompoundCalc</span>
            </a>
            <a href="{calc_url}" class="text-indigo-400 hover:text-indigo-300 text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-16">
        <article class="max-w-3xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl md:text-4xl font-bold mb-4">{t['h1']}</h1>
                <p class="text-slate-400">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-10 prose">
                <p class="text-lg">{t['intro']}</p>
                
                <h2>{t['what_simple_title']}</h2>
                <p>{t['what_simple']}</p>
                <div class="formula">{t['simple_formula']}</div>
                <h3>{t['simple_example_title']}</h3>
                <p>{t['simple_example']}</p>
                
                <h2>{t['what_compound_title']}</h2>
                <p>{t['what_compound']}</p>
                <div class="formula">{t['compound_formula']}</div>
                <p class="text-sm text-slate-500">{t['compound_formula_note']}</p>
                <h3>{t['compound_example_title']}</h3>
                <p>{t['compound_example']}</p>
                
                <h2>{t['difference_title']}</h2>
                <p>{t['difference']}</p>
                
                <h2>{t['table_title']}</h2>
                <div class="overflow-x-auto my-4">
                    <table class="w-full text-sm">
                        <thead>
                            <tr class="border-b border-white/10">
                                <th class="py-2 text-left text-slate-400">{t['table_years']}</th>
                                <th class="py-2 text-right text-slate-400">{t['table_simple']}</th>
                                <th class="py-2 text-right text-slate-400">{t['table_compound']}</th>
                                <th class="py-2 text-right text-slate-400">{t['table_diff']}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-white/5"><td class="py-2">10</td><td class="py-2 text-right">$17,000</td><td class="py-2 text-right">$19,672</td><td class="py-2 text-right text-green-400">+$2,672</td></tr>
                            <tr class="border-b border-white/5"><td class="py-2">20</td><td class="py-2 text-right">$24,000</td><td class="py-2 text-right">$38,697</td><td class="py-2 text-right text-green-400">+$14,697</td></tr>
                            <tr class="border-b border-white/5"><td class="py-2">30</td><td class="py-2 text-right">$31,000</td><td class="py-2 text-right">$76,123</td><td class="py-2 text-right text-green-400">+$45,123</td></tr>
                            <tr><td class="py-2">40</td><td class="py-2 text-right">$38,000</td><td class="py-2 text-right">$149,745</td><td class="py-2 text-right text-green-400">+$111,745</td></tr>
                        </tbody>
                    </table>
                </div>
                
                <h2>{t['when_title']}</h2>
                <h3>{t['when_simple_title']}</h3>
                <ul>{when_simple_items}</ul>
                <h3>{t['when_compound_title']}</h3>
                <ul>{when_compound_items}</ul>
                
                <h2>{t['key_title']}</h2>
                <ul>
                    <li>{t['key_1']}</li>
                    <li>{t['key_2']}</li>
                    <li>{t['key_3']}</li>
                    <li>{t['key_4']}</li>
                </ul>
                
                <div class="mt-8 p-6 bg-indigo-500/10 rounded-xl border border-indigo-500/30">
                    <p class="text-indigo-400 font-semibold mb-2">📊 {t['cta_title']}</p>
                    <p class="mb-4">{t['cta_text']}</p>
                    <a href="{calc_url}" class="inline-block bg-indigo-500 hover:bg-indigo-600 text-white font-semibold px-6 py-3 rounded-xl transition">{t['cta_button']}</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="py-8 px-4 border-t border-white/10">
        <div class="max-w-3xl mx-auto text-center text-slate-500 text-sm">
            <p>© 2026 CompoundCalc.ai</p>
        </div>
    </footer>
</body>
</html>'''


def generate_beginners_guide(t, lang, calc_url):
    """Generate beginner's guide article."""
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    
    # Build lists
    rule72_items = ''.join([f'<li>{item}</li>' for item in t['rule72_examples']])
    freq_items = ''.join([f'<li>{item}</li>' for item in t['frequency_list']])
    common_items = ''.join([f'<li>{item}</li>' for item in t['common_list']])
    
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <meta name="description" content="{t['meta']}">
    <link rel="canonical" href="https://compoundcalc.ai/articles/beginners-guide/{'' if lang == 'en' else lang + '/'}">
    
    <meta property="og:title" content="{t['h1']}">
    <meta property="og:description" content="{t['meta']}">
    <meta property="og:type" content="article">
    
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{t['h1']}","description":"{t['meta']}","author":{{"@type":"Organization","name":"CompoundCalc.ai"}},"publisher":{{"@type":"Organization","name":"CompoundCalc.ai"}},"datePublished":"2026-02-20","dateModified":"2026-02-20"}}
    </script>
    
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%236366f1'/%3E%3Ctext x='50' y='68' font-size='50' text-anchor='middle' fill='white'%3E📈%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); min-height: 100vh; }}
        .glass {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
        .prose {{ line-height: 1.8; }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #818cf8; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #c4b5fd; }}
        .prose p {{ margin-bottom: 1rem; color: #cbd5e1; }}
        .prose ul, .prose ol {{ margin-left: 1.5rem; margin-bottom: 1rem; color: #cbd5e1; }}
        .prose ul {{ list-style: disc; }}
        .prose ol {{ list-style: decimal; }}
        .prose li {{ margin-bottom: 0.5rem; }}
        .prose strong {{ color: #f1f5f9; }}
        .formula {{ background: rgba(99,102,241,0.2); border: 1px solid rgba(99,102,241,0.4); padding: 1rem; border-radius: 0.75rem; font-family: monospace; text-align: center; margin: 1rem 0; color: #c4b5fd; font-size: 1.25rem; }}
        .step {{ background: rgba(255,255,255,0.03); border-left: 3px solid #818cf8; padding: 1rem; margin: 0.5rem 0; }}
    </style>
    
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-540W3EEBWX"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-540W3EEBWX');</script>
</head>
<body class="text-white">
    <header class="py-6 px-4">
        <div class="max-w-3xl mx-auto flex items-center justify-between">
            <a href="{calc_url}" class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-600 flex items-center justify-center text-xl">📈</div>
                <span class="text-xl font-bold">CompoundCalc</span>
            </a>
            <a href="{calc_url}" class="text-indigo-400 hover:text-indigo-300 text-sm">{t['back']}</a>
        </div>
    </header>

    <main class="px-4 pb-16">
        <article class="max-w-3xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl md:text-4xl font-bold mb-4">{t['h1']}</h1>
                <p class="text-slate-400">{t['subtitle']}</p>
            </div>

            <div class="glass rounded-2xl p-6 md:p-10 prose">
                <p class="text-lg">{t['intro']}</p>
                
                <h2>{t['what_title']}</h2>
                <p>{t['what_text']}</p>
                <p class="italic text-indigo-300">{t['what_analogy']}</p>
                
                <h2>{t['how_title']}</h2>
                <div class="step">
                    <p class="font-semibold text-indigo-300">{t['how_step1_title']}</p>
                    <p class="mb-0">{t['how_step1']}</p>
                </div>
                <div class="step">
                    <p class="font-semibold text-indigo-300">{t['how_step2_title']}</p>
                    <p class="mb-0">{t['how_step2']}</p>
                </div>
                <div class="step">
                    <p class="font-semibold text-indigo-300">{t['how_step3_title']}</p>
                    <p class="mb-0">{t['how_step3']}</p>
                </div>
                <p class="mt-4 p-4 bg-indigo-500/10 rounded-xl">{t['how_note']}</p>
                
                <h2>{t['magic_title']}</h2>
                <p>{t['magic_text']}</p>
                <div class="overflow-x-auto my-4">
                    <table class="w-full text-sm">
                        <thead>
                            <tr class="border-b border-white/10">
                                <th class="py-2 text-left text-slate-400">{t['magic_table_years']}</th>
                                <th class="py-2 text-right text-slate-400">{t['magic_table_value']}</th>
                                <th class="py-2 text-right text-slate-400">{t['magic_table_earned']}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-white/5"><td class="py-2">10</td><td class="py-2 text-right">$19,672</td><td class="py-2 text-right text-green-400">$9,672</td></tr>
                            <tr class="border-b border-white/5"><td class="py-2">20</td><td class="py-2 text-right">$38,697</td><td class="py-2 text-right text-green-400">$28,697</td></tr>
                            <tr class="border-b border-white/5"><td class="py-2">30</td><td class="py-2 text-right">$76,123</td><td class="py-2 text-right text-green-400">$66,123</td></tr>
                            <tr><td class="py-2">40</td><td class="py-2 text-right">$149,745</td><td class="py-2 text-right text-green-400">$139,745</td></tr>
                        </tbody>
                    </table>
                </div>
                
                <h2>{t['rule72_title']}</h2>
                <p>{t['rule72_text']}</p>
                <div class="formula">{t['rule72_formula']}</div>
                <h3>{t['rule72_examples_title']}</h3>
                <ul>{rule72_items}</ul>
                
                <h2>{t['frequency_title']}</h2>
                <p>{t['frequency_text']}</p>
                <ul>{freq_items}</ul>
                <p class="text-sm text-slate-500">{t['frequency_note']}</p>
                
                <h2>{t['start_title']}</h2>
                <p>{t['start_text']}</p>
                <ul>
                    <li>{t['start_alice']}</li>
                    <li>{t['start_bob']}</li>
                </ul>
                <p class="p-4 bg-green-500/10 rounded-xl border border-green-500/30">{t['start_result']}</p>
                <p><strong>{t['start_lesson']}</strong></p>
                
                <h2>{t['tips_title']}</h2>
                <ol>
                    <li>{t['tip1']}</li>
                    <li>{t['tip2']}</li>
                    <li>{t['tip3']}</li>
                    <li>{t['tip4']}</li>
                    <li>{t['tip5']}</li>
                </ol>
                
                <h2>{t['common_title']}</h2>
                <ul>{common_items}</ul>
                
                <h2>{t['warning_title']}</h2>
                <p class="p-4 bg-red-500/10 rounded-xl border border-red-500/30">{t['warning_text']}</p>
                
                <div class="mt-8 p-6 bg-indigo-500/10 rounded-xl border border-indigo-500/30">
                    <p class="text-indigo-400 font-semibold mb-2">🧮 {t['cta_title']}</p>
                    <p class="mb-4">{t['cta_text']}</p>
                    <a href="{calc_url}" class="inline-block bg-indigo-500 hover:bg-indigo-600 text-white font-semibold px-6 py-3 rounded-xl transition">{t['cta_button']}</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="py-8 px-4 border-t border-white/10">
        <div class="max-w-3xl mx-auto text-center text-slate-500 text-sm">
            <p>© 2026 CompoundCalc.ai</p>
        </div>
    </footer>
</body>
</html>'''


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate compound vs simple articles
    print("Generating compound-vs-simple articles...")
    for lang, t in COMPOUND_VS_SIMPLE.items():
        lang_info = LANGUAGES.get(lang, {'dir': lang})
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'articles', 'compound-vs-simple')
            calc_url = '/'
        else:
            out_dir = os.path.join(base_dir, 'articles', 'compound-vs-simple', lang)
            calc_url = f'/{lang}/'
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_compound_vs_simple(t, lang, calc_url)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    # Generate beginner's guide articles
    print("\nGenerating beginners-guide articles...")
    for lang, t in BEGINNERS_GUIDE.items():
        lang_info = LANGUAGES.get(lang, {'dir': lang})
        
        if lang == 'en':
            out_dir = os.path.join(base_dir, 'articles', 'beginners-guide')
            calc_url = '/'
        else:
            out_dir = os.path.join(base_dir, 'articles', 'beginners-guide', lang)
            calc_url = f'/{lang}/'
        
        os.makedirs(out_dir, exist_ok=True)
        html = generate_beginners_guide(t, lang, calc_url)
        
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ {lang}")
    
    print(f"\n🎉 Generated 22 article pages (2 articles × 11 languages)!")


if __name__ == '__main__':
    main()
