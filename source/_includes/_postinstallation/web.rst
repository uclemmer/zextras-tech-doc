
The first task to carry out is to change the password of the
``zextras`` user. This is a very important task, because this user has
full powers over all |product| functionalities, therefore its password
must be robust. More details and the command to change the password
can be found in section :ref:`manage-admins`.

After you change the password, point a :ref:`supported browser
<browser_compatibility>` to the Proxy Node's IP or hostname and port
*6071* (e.g., https://172.16.0.12:6071/) and log in to the |adminui|,
with user ``zextras@example.com`` and password the one you just
changed.

If the login is successful, go to **Domains**, select the domain
example.com, and, under the **General Settings** and define:

* The **Public Server Host Name**, setting it as
  *https://mail.example.com*

* The **Public Service Port**, setting it as *443*.

These two values combined represent the URL that users need
to access to use the features of |product|.

.. note:: Since |product| uses SSL, it is strongly suggested to
   install an SSL certificate. Please refer to Section
   :ref:`install-SSL-cert` (CLI) or :ref:`ap-vhost` |adminui| for
   directions. You can even install a :ref:`Let's Encrypt certificate
   <le-procedure>`.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Web Client
      :columns: 6
      
      The web client is used by :term:`regular users <Regular User>` to access to the
      e-mail account and can be used also to access other
      functionalities (|file|, |docs| if installed), as well as other
      client protocols such as IMAP or POP, and is available at
      https://mail.example.com/. In :ref:`carbonio-usage` you can find
      directions that guide you in your first steps with |product| and
      introduction to the most common tasks


   .. grid-item-card:: |adminui|
      :columns: 6

      The |adminui| is used for Administration access and is available at:
      https://mail.example.com:6071/

      Here, you can manage server, domains, accounts, and other
      configurations. Please refer to section :ref:`adminpanel` for
      more information.

Regardless of the language configured on |product|, the locale set on
the browser takes precedence: This means that dates, currency, and
other locale-related values will be displayed according to the
language of the browser, which is usually inherited by the locale set
for the operating system.

Multiple Configured Domains
===========================

When multiple domains are defined on |product|, you will see in the
*username* field, the default domain: to log in to that domain, you
can use only the username. To login to another domain, you need to
write the whole e-mail address: username and domain.
