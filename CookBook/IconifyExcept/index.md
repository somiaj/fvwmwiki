---
layout : wiki
title : IconifyExcept
type : recipe
description : |
  This will Iconfiy every window except one.
---

## Iconifying all windows except one.

To Iconify all windows except one (or all but a certain group of windows)
in Fvwm there are various ways. One way is to use the !Iconifiable style on the
windows you want to disclude the possibility of being iconified:

{% highlight fvwm %}
Style FvwmButtons !Iconifiable
{% endhighlight %}

Then, to iconify windows on the current page, one might use:

{% highlight fvwm %}
All (CurrentPage, !Iconic) Iconify
{% endhighlight %}

This can be attached to a key binding, or a mouse binding, or put it
as part of a complex function that could get called.

The All conditional will preform the Iconfiy action on all windows that satisfy
the conditions listed, which in this example are windows on the CurrentPage
and that are not Iconic.

Conditions can also include a windows name/class/resource. Thus you can use
the following to Iconify all windows whose name/class/resource doesn't match
MyWindowName as follows:

{% highlight fvwm %}
All (CurrentPage, !Iconic, !MyWindowName) Iconify
{% endhighlight %}

As another option you could Iconify all windows except the window that has focus
by adding the !Focused condition.

{% highlight fvwm %}
All (CurrentPage, !Iconic, !Focused) Iconify
{% endhighlight %}

