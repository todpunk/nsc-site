# -*- coding: utf-8 -*-
import os
from pydozer import Page

about_page = Page()
about_page.data['filename'] = os.path.basename(__file__).replace('.pyc', '').replace('.py', '')

about_page.data['title'] = "Network Sanitation Committee - About"
about_page.data['is_home'] = False
about_page.data['content'] = """
                        <div class="row">
                            <div class="12u">

                                <!-- Intro -->
                                    <section id="intro">
                                        <div class="row">
                                            <div class="12u">
                                                <p>NSC was started with a single motivation: Make simple tools for managing the way we communicate every day.  We understand that the issue with today's technology and media is a lack of options for consumers to control the way they are contacted.</p>
                                                <p>We've started making things better for everyone with <a href="https://phonejanitor.com/">Phone Janitor</a>, a service that gives you all the power of a personal receptionist.  Remember as a kid when you were excited to answer the phone, maybe even competing with siblings to pick up?  Well, now we have that feeling as adults.</p>
                                                <p>We have other projects in the works.  Feel free to email us at <a href="mailto:feedback@networksanitationcommittee.com">feedback@networksanitationcommittee.com</a> and let us know what your ideas are.  <a href="https://phonejanitor.com/app/#signup">Sign up</a> for service to improve your own life, and help us further development to make the web actually better, for you and everyone else.</p>
                                            </div>
                                        </div>
                                    </section>
                            </div>
                        </div>
"""
