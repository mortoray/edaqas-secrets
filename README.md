# Edaqa's Secret Sharing

_Use this tool to allow friends, colleagues, and loved ones, gain access to your systems in case of an emergency. It allows you to break a secret into parts, and if enough recipients agree to combine their parts, the initial secret can be recovered._

This project allows you to create a shared secret, where a given number of people can combine their code to get the secret.

# Goals

- The UX needs to be accessible to people of any technical literacy. It's important that recipients do not need to involve third-parties to help them restore secrets.
- The encoded needs to be paranoid and usable without a network connection. It is therefore a single HTML page.
- The encoding must be future proof to loss of this project, algorithm changes, or deployment restrictions. Therefore a single-page HTML app is to be provided to all recipients.
- The code must be auditable. To this end the output program is not minimized or obfuscated in any way.  (I believe the Shamir algorithm code is still too complicated, and can be reduced.)

# License

You are granted the license to use this product, even in an offline setting. The results, for reconstruction, may be freely shared.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Acknowledgements

## secrets.js

Parts of this code are taken from secrets.js which carries the below license. If you need a Shamir libary, start at [that project](https://github.com/grempe/secrets.js), since the code here may not in a good form.

Copyright (c) 2012 Alexander Stetsyuk
Copyright (c) 2014-2019 Glenn Rempe

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

