[![publish](https://github.com/bankruptko/vaccination-results-jp/actions/workflows/publish.yml/badge.svg?branch=master)](https://github.com/bankruptko/vaccination-results-jp/actions/workflows/publish.yml)
## Japan COVID-19 Vaccination result

https://bankruptko.github.io/vaccination-results-jp/

厚生労働省の[新型コロナワクチンの接種実績](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/vaccine_sesshujisseki.html)ページおよび首相官邸ウェブサイトの[新型コロナワクチンについて](https://www.kantei.go.jp/jp/headline/kansensho/vaccine.html)ページから日本における新型コロナワクチンの接種実績情報を取得し、扱いやすい形式にデータを加工・連結した上で GitHub Pages による可視化を行います。

- [GitHub Pages による可視化ページはこちら](https://bankruptko.github.io/vaccination-results-jp/)
- [GitHub Flat Viewer による可視化ページはこちら](https://flatgithub.com/bankruptko/vaccination-results-jp?filename=data%2Fdata.csv)

## TODO

- [ ] 厚生労働省のウェブサイトから 2021/04/09 までの接種実績データを取得し CSV ファイルへと変換する
- [x] 首相官邸ウェブサイトの Excel ファイル（.xlxs）を取得し CSV ファイル（.csv）へと変換する
- [x] 変換した CSV データを正規化する
- [ ] 正規化した CSV データを連結する
- [x] GitHub Pages による可視化を行う

## License

See [LICENSE](https://github.com/bankruptko/vaccination-results-jp/blob/master/LICENSE).