# -*- coding: utf-8 -*-
import os
from pydozer import Page

index_page = Page()
index_page.data['filename'] = os.path.basename(__file__).replace('.pyc', '').replace('.py', '')

index_page.data['title'] = "Network Sanitation Committee - Clean up the Net"
index_page.data['is_home'] = True
index_page.data['banner'] = """
                            <div id="banner">
                                <section>
                                    <h2>We're the Network Sanitation Committee</h2>
                                    <p>We make simple, clean software services.</p>
                                </section>
                            </div>
"""
index_page.data['content'] = """
                        <div class="row">
                            <div class="12u">

                                <!-- Intro -->
                                    <section id="intro">
                                        <div class="row">
                                            <div class="4u 12u(mobile)">
                                                <section class="first">
                                                    <span class="pennant"><span class="icon fa-phone-square"></span></span>
                                                    <h3><a href="https://phonejanitor.com/?origin_tag=nsc_cta">Phone Janitor</a></h3>
                                                    <p>A phone number you control, built to make calls happy again.</p>
                                                </section>
                                            </div>

                                            <div class="4u 12u(mobile)">
                                                <section class="middle">
                                                    <span class="pennant"><span class="icon fa-simplybuilt"></span></span>
                                                    <h3>Simple Ideas</h3>
                                                    <p>Our projects make the internet less complicated, for everyone.</p>
                                                </section>
                                            </div>

                                            <div class="4u 12u(mobile)">
                                                <section class="last">
                                                    <span class="pennant"><span class="icon fa-cogs"></span></span>
                                                    <h3>Configurable</h3>
                                                    <p>Make it your way, with more peace that it's yours, always.</p>
                                                </section>
                                            </div>

                                        </div>
                                    </section>

                            </div>
                        </div>
"""
