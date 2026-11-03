# AlarmMate Sensors privacy, use and support

Public static website for AlarmMate Sensors (AlarmMate) for iOS, intended for academic use, learning and sensor experiments. Event history stays on the device and can be exported as a CSV file.

- Website: https://pcbcontrol.github.io/alarmmate-support/
- Privacy policy (English): https://pcbcontrol.github.io/alarmmate-support/privacy/
- Use, safety and limitations: https://pcbcontrol.github.io/alarmmate-support/usage/
- Support: https://pcbcontrol.github.io/alarmmate-support/support/

Responsible person: Francesc Roig. Contact: mutton-purge1s@icloud.com.

The intended-use notice explains academic use and operating risks. It supplements the applicable licence and preserves mandatory rights; it does not establish a custom EULA or guarantee an exemption from liability. The standard reference is Apple's Licensed Application End User License Agreement: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/

GitHub Pages uses the `Publish English website` Actions workflow. Its artifact contains only the English pages, shared assets and compatibility redirects. The Catalan HTML files in `ca/` are retained in this repository for future reuse and are not included in the published artifact. The website uses HTML and CSS with no scripts, external fonts, analytics, forms, or advertising. `.nojekyll` enables direct static publishing.

To update a page, edit the corresponding `index.html`. Only the English version is published. Do not delete or overwrite the retained Catalan source files. Former Catalan URLs redirect to their English equivalents and are excluded from the sitemap. The workflow builds its artifact with `python3 tools/build_pages.py --output _site` and uploads only `_site`, not the repository root. Update the policy date when its substance changes. These pages describe the AlarmMate iOS app. Check actual data handling before extending the policy to another app or platform.

The app source, firmware, and credentials are not included in this repository.
